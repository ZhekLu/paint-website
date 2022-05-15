from django.urls import path

from testhtml.views import index, index_paint, old_paint_index

urlpatterns = [
    path('1', index_paint),
    path('2', old_paint_index),
    path('3', index),
]
