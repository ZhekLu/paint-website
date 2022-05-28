from django.urls import path

from .views import pps, PPDetailView, comments

urlpatterns = [
    path('pps/<int:pk>/comments/', comments),
    path('pps/<int:pk>/', PPDetailView.as_view()),
    path('pps/', pps),
]