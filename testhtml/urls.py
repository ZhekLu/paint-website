from django.urls import path

from testhtml.views import index

urlpatterns = [
    path('', index),
]
