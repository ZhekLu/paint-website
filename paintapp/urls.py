from django.urls import path

from paintapp.views import old_paint, new_paint, info

app_name = 'paintapp'
urlpatterns = [
    path('info', info, name='info'),
    path('old', old_paint, name='old_paint'),
    path('', new_paint, name='new_paint'),
]
