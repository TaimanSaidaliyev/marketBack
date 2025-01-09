from django.urls import path

from .views import *

urlpatterns = [
    path('product/add/', ProductStatisticsView.as_view(),),
    path('product/get/', ProductStatisticsView.as_view(),),
    path('shop/add/', ShopStatisticsView.as_view(),),
    path('shop/get/', ShopStatisticsView.as_view(),),
    path('shop/period/', ShopStatisticsByPeriodAPIView.as_view(),),
    # path('shop/region/', ShopStatisticsByRegionAPIView.as_view()),
    path('product/period/', ProductStatisticsByPeriodAPIView.as_view()),
    # path('product/region/', ProductStatisticsByRegionAPIView.as_view()),
    path('shop/<int:shop_id>/period/', SingleShopStatisticsByPeriodAPIView.as_view(),),
    path('product/<int:product_id>/period/', SingleProductStatisticsByPeriodAPIView.as_view(),),
]