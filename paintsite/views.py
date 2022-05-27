from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator
from django.core.signing import BadSignature
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import UpdateView, CreateView, TemplateView, DeleteView

from paintsite.forms import ChangeUserInfoForm, RegisterUserForm, SearchForm
from paintsite.models import User, SubTag, PictureBoard
from paintsite.utilities import signer


def index(request):
    pps = PictureBoard.objects.filter(is_public=True)[:10]
    context = {'pps': pps}
    return render(request, 'paintsite/index.html', context)


def other_page(request, page):
    try:
        template = get_template('paintsite/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


@login_required
def profile(request):
    context = {'pps': PictureBoard.objects.filter(author=request.user.pk)}
    return render(request, 'paintsite/profile.html', context)


class PSLoginView(LoginView):
    template_name = 'paintsite/login.html'


class PSLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'paintsite/logout.html'


# Change Views


class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'paintsite/change_user_info.html'
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
    template_name = 'paintsite/password_change.html'
    success_url = reverse_lazy('paintsite:profile')
    success_message = 'Password was changed.'


# Registration


class RegisterUserView(CreateView):
    model = User
    template_name = 'paintsite/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('paintsite:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'paintsite/register_done.html'


# Activation

def user_activate(request, sign):
    try:
        username = signer.unsign(sign)
    except BadSignature:
        return render(request, 'paintsite/bad_signature.html')

    user = get_object_or_404(User, username=username)
    if user.is_activated:
        template = 'paintsite/user_is_activated.html'
    else:
        template = 'paintsite/activation_done.html'
        user.is_active = True
        user.is_activated = True
        user.save()
    return render(request, template)


class DeleteUserView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'paintsite/delete_user.html'
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
    pps = PictureBoard.objects.filter(is_public=True, tag=pk)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        q = Q(title__icontains=keyword) | Q(description__icontains=keyword)
        pps = pps.filter(q)
    else:
        keyword = ''

    form = SearchForm(initial={'keyword': keyword})
    paginator = Paginator(pps, 2)
    if 'page' in request.GET:
        page_num = request.GET['page']
    else:
        page_num = 1
    page = paginator.get_page(page_num)
    context = {'tag': tag, 'page': page, 'pps': page.object_list, 'form': form}
    return render(request, 'paintsite/by_tag.html', context)


def detail(request, tag_pk, pk):
    pp = get_object_or_404(PictureBoard, pk=pk)
    context = {'pp': pp}
    return render(request, 'paintsite/detail.html', context)


@login_required
def profile_pp_detail(request, pk):
    pp = get_object_or_404(PictureBoard, pk=pk)
    context = {'pp': pp}
    return render(request, 'paintsite/profile_detail.html', context)
