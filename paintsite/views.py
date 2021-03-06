import asyncio

from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.sites.shortcuts import get_current_site
from django.core.paginator import Paginator
from django.core.signing import BadSignature
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.template.exceptions import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, TemplateView, DeleteView

from paintsite.coroutines import get_pps, get_comments
from paintsite.forms import ChangeUserInfoForm, RegisterUserForm, SearchForm, PictureForm, UserCommentForm, \
    GuestCommentForm, LoginForm, PSPasswordChangeForm
from paintsite.models import User, SubTag, PictureBoard
from paintsite.utilities import signer


def index(request):
    pps = asyncio.run(get_pps(is_public=True))[:10]
    context = {'pps': pps}
    return render(request, 'paintsite/home/index.html', context)


def other_page(request, page):
    try:
        template = get_template('paintsite/home/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


@login_required
def profile(request):
    context = {'pps': asyncio.run(get_pps(author=request.user.pk))}
    return render(request, 'paintsite/profile/profile.html', context)


class PSLoginView(LoginView):
    form_class = LoginForm
    template_name = 'paintsite/authentication/login.html'


class PSLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'paintsite/authentication/logout.html'


# Change Views


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'paintsite/profile/profile_edit.html'
    form_class = ChangeUserInfoForm
    success_url = reverse_lazy('paintsite:profile')
    success_message = 'Personal data was changed.'

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


class PSPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin, PasswordChangeView):
    form_class = PSPasswordChangeForm
    template_name = 'paintsite/profile/profile_password_change.html'
    success_url = reverse_lazy('paintsite:profile')
    success_message = 'Password was changed.'


# Registration


class RegisterUserView(CreateView):
    model = User
    template_name = 'paintsite/authentication/register.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('paintsite:register_done')

    def get_form_kwargs(self):
        kwargs = super(RegisterUserView, self).get_form_kwargs()
        current_site = get_current_site(self.request)
        kwargs.update({'domain': current_site.domain})
        return kwargs


class RegisterDoneView(TemplateView):
    template_name = 'paintsite/authentication/register_done.html'


# Activation

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'paintsite/authentication/bad_signature.html')

    user = get_object_or_404(User, username=username)
    if user.is_activated:
        template = 'paintsite/authentication/user_is_activated.html'
    else:
        template = 'paintsite/authentication/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'paintsite/profile/profile_delete.html'
    success_url = reverse_lazy('paintsite:index')

    def setup(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().setup(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        logout(request)
        messages.add_message(request, messages.SUCCESS, 'User was deleted.')
        return super().post(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)


def by_tag(request, pk):
    tag = get_object_or_404(SubTag, pk=pk)
    pps = asyncio.run(get_pps(is_public=True, tag=pk))
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword)
        pps = pps.filter(q)
    else:
        keyword = ''

    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(pps, 6)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'tag': tag, 'page': page, 'pps': page.object_list, 'form': form}
    return render(request, 'paintsite/home/by_tag.html', context)


# Picture Posts

def get_detail_context(request, pk):
    pp = PictureBoard.objects.get(pk=pk)
    comments = asyncio.run(get_comments(pp=pk, is_active=True))
    initial = {'pp': pp.pk}
    if request.user.is_authenticated:
        initial['author'] = request.user.username
        form_class = UserCommentForm
    else:
        form_class = GuestCommentForm
    form = form_class(initial=initial)

    if request.method == 'POST':
        c_form = form_class(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.add_message(request, messages.SUCCESS, 'Comment was added')
        else:
            form = c_form
            messages.add_message(request, messages.WARNING, 'Comment was not added')

    return {'pp': pp, 'comments': comments, 'form': form}


def detail(request, tag_pk, pk):
    return render(request, 'paintsite/home/pp_detail.html', get_detail_context(request, pk))


@login_required
def profile_pp_detail(request, pk):
    return render(request, 'paintsite/profile/profile_pp_detail.html', get_detail_context(request, pk))


@login_required
def profile_pp_add(request):
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Picture was published')
            return redirect('paintsite:profile')
    else:
        form = PictureForm(initial={'author': request.user.pk})
    context = {'form': form}
    return render(request, 'paintsite/profile_pp_add.html', context)


@login_required
def profile_pp_change(request, pk):
    pp = get_object_or_404(PictureBoard, pk=pk)
    if request.method == 'POST':
        form = PictureForm(request.POST, request.FILES, instance=pp)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Picture was changed')
            return redirect('paintsite:profile')
    else:
        form = PictureForm(instance=pp)
    context = {'form': form}
    return render(request, 'paintsite/profile_pp_change.html', context)


@login_required
def profile_pp_delete(request, pk):
    pp = get_object_or_404(PictureBoard, pk=pk)
    if request.method == 'POST':
        pp.delete()
        messages.add_message(request, messages.SUCCESS, 'Picture was deleted')
        return redirect('paintsite:profile')
    else:
        context = {'pp': pp}
        return render(request, 'paintsite/profile/profile_pp_delete.html', context)

