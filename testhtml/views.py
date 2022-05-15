from django.shortcuts import render


def index(request):
    return render(request, 'testhtml/index.html')


def index_paint(request):
    return render(request, 'testhtml/index_paint.html')


def old_paint_index(request):
    return render(request, 'testhtml/old_paint.html')
