from django.urls import path

from .views import pps

urlpatterns = [
    path('pps/', pps),
]