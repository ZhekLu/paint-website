from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template
from django.contrib.auth.views import LoginView, LogoutView

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
