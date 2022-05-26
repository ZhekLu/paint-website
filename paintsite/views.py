from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.urls import reverse_lazy
from django.views.generic import UpdateView

from paintsite.forms import ChangeUserInfoForm
from paintsite.models import User


def index(request):
    return render(request, 'paintsite/index.html')


def other_page(request, page):
    try:
        template = get_template('paintsite/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))


@login_required
def profile(request):
    return render(request, 'paintsite/profile.html')


class PSLoginView(LoginView):
    template_name = 'paintsite/login.html'


class PSLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'paintsite/logout.html'


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
