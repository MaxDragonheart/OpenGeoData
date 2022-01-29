from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from filebrowser.sites import site

urlpatterns = [
    path('site-adminpanel/', include([
        path('filebrowser/', site.urls),
        path('grappelli/', include('grappelli.urls')),
        path('', admin.site.urls),
        path('tinymce/', include('tinymce.urls')),
    ])),
    path('', include('base.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)