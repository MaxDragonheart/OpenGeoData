from django.urls import include, path

from . import views


urlpatterns = [
    path('gis/', include([
        path('test/', include([
            path('', views.test_map, name='test-map'),
            path('<int:pk>/', views.test_map_single, name='test-map-single'),
        ])),
        path('', views.wms_list, name='wms-list'),
        path('<slug:slug_post>/', views.single_wms, name='wms-single'),
    ])),
]