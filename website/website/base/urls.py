from django.urls import include, path

from . import views


urlpatterns = [
    path('', views.index, name='index'),
    # path('', include([
    #     path('', views.sharedtag_list, name='index'),
    #     path('<slug:slug>/', views.single_shared, name='sharedtag-single'),
    # ])),
    path('', include('gismanager.urls')),
    path('', include('usermanager.urls')),
]