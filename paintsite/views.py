from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.template import TemplateDoesNotExist
from django.template.loader import get_template


def index(request):
    return render(request, 'paintsite/index.html')


def other_page(request, page):
    try:
        template = get_template('paintsite/' + page + '.html')
    except TemplateDoesNotExist:
        raise Http404
    return HttpResponse(template.render(request=request))

