from django.urls import include, path

from . import views


urlpatterns = [
    path('gis/', include([
        path('', views.wms_list, name='wms-list'),
        path('<slug:slug_post>/', views.single_wms, name='wms-single'),
    ])),
]