from django.shortcuts import render


def old_paint(request):
    return render(request, 'paintapp/old_paint.html')


def new_paint(request):
    return render(request, 'paintapp/new_paint.html')


def info(request):
    return render(request, 'paintapp/info.html')
