from django.urls import path

from .views import pps, PPDetailView

urlpatterns = [
    path('pps/<int:pk>', PPDetailView.as_view()),
    path('pps/', pps),
]