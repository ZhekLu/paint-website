from django.urls import path

from paintapp.views import index

urlpatterns = [
    path('', index),
]
