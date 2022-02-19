from django.urls import include, path

from . import views


urlpatterns = [
    path('gis/', include([
        path('test/', include([
            path('', views.test_map),
            path('<int:id>/', views.test_map_single),
        ])),
        path('geodata/', include([
            path('', views.wms_list, name='wms-list'),
            path('<slug:slug_post>/', views.single_wms, name='wms-single'),
        ])),
        path('map/', include([
            path('', views.webgis_list, name='map'),
            path('<slug:slug_post>/', views.single_webgis, name='map-single'),
        ])),
    ])),
]