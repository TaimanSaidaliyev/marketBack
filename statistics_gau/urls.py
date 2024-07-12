from django.urls import path

from .views import *

urlpatterns = [
    path('product/add/', ProductStatisticsView.as_view(),),
    path('product/get/', ProductStatisticsView.as_view(),),
    path('shop/add/', ShopStatisticsView.as_view(),),
    path('shop/get/', ShopStatisticsView.as_view(),),
]