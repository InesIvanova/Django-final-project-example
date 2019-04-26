from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.FurnitureList.as_view(), name='furniture'),
    path('mine/', views.UserFurnitureList.as_view(), name='user-furniture'),
    re_path('^details/(?P<pk>\d+)/$', views.FurnitureDetail.as_view(), name='furniture-detail'),
    re_path('^delete/(?P<pk>\d+)/$', views.FurnitureDelete.as_view(), name='furniture-delete')

]