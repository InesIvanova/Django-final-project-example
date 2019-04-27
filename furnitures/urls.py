from django.urls import path, re_path

from . import views
from reviews import views as review_views

urlpatterns = [
    path('', views.FurnitureList.as_view(), name='furniture'),
    path('material/', views.CreateMaterial.as_view(), name='material-add'),
    path('mine/', views.UserFurnitureList.as_view(), name='user-furniture'),
    re_path('^details/(?P<pk>\d+)/$', views.FurnitureDetail.as_view(), name='furniture-detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.FurnitureDelete.as_view(), name='furniture-delete'),
    #re_path('^details/(?P<pk>\d+)/review/$', review_views.testrender, name='review')
    re_path('^create/$', views.FurnitureCreate.as_view(), name='furniture-create'),
    re_path('^edit/(?P<pk>\d+)/$', views.FurnitureEdit.as_view(), name='furniture-edit')

]