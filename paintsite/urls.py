from django.urls import path

from paintsite.views import index, other_page

app_name = 'paintsite'

urlpatterns = [
    path('<str:page>/', other_page, name='other'),
    path('', index, name='index'),
]
