from django.urls import include, path

from . import views


urlpatterns = [
    # path('test-gis/', include([
    #     path('', views.test_map),
    #     path('<int:id>/', views.test_map_single),
    # ])),
    path('wms/', include([
        path('', views.wms_list, name='wms-list'),
        path('<slug:slug>/', views.single_wms, name='ogc-single'),
    ])),
    path('map/', include([
        path('', views.webgis_list, name='map'),
        path('<slug:slug>/', views.single_webgis, name='map-single'),
    ])),
]