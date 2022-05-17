from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.utils.translation import gettext as _

from gismanager.views import search
from base.views import organogram

urlpatterns = [
    path(f'{settings.ADMIN_PANEL}/', include([
        path('', admin.site.urls),
    ])),
    path('', include('core.urls')),
]

urlpatterns += i18n_patterns(
    path(_('risultati/'), search, name='search-results'),
    path(_('organigramma/'), organogram, name='organogram')
)


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
