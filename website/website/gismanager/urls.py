from django.urls import include, path

from . import views


urlpatterns = [
    path('gis/', views.wms_list, name='wms-list'),
]