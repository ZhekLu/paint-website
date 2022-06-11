from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.views import serve
from django.views.decorators.cache import never_cache

from paintweb.settings.production import STATIC_ROOT, MEDIA_ROOT

urlpatterns = [
    path('paintapp/', include('paintapp.urls')),
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('api/', include('api.urls')),
    path('', include('paintsite.urls')),
]

if settings.DEBUG:
    urlpatterns.insert(0, path('static/<path:path>', never_cache(serve)))
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
else:
    urlpatterns.insert(0, re_path(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}))
    urlpatterns.insert(0, re_path(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}))
