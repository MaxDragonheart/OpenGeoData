from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

from .sitemaps import (
                        StaticSitemap,
                        SharedCategoriesSitemap,
                        OGCLayerSitemap, WebGISProjectSitemap
                    )
sitemaps = {
    'staticpage': StaticSitemap,
    'shared-category': SharedCategoriesSitemap,
    'ogc-layer': OGCLayerSitemap,
    'webgis-project': WebGISProjectSitemap
}


urlpatterns = [
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('base.urls')),
    path('', include('gismanager.urls')),
    path('', include('usermanager.urls')),
]
