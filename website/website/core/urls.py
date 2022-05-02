from django.urls import path, include
from django.contrib.sitemaps.views import sitemap

urlpatterns = [
    #path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
    path('', include('base.urls')),
    path('', include('gismanager.urls')),
    path('', include('usermanager.urls')),
]