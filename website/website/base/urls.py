from django.urls import include, path

from . import views


urlpatterns = [
    #path('', views.index, name='index'),
    path('', include([
        path('', views.sharedcategories_list, name='index'),
        path('category/<slug:slug>/', views.single_sharedcategory, name='single-sharedcategory'),
    ])),
]