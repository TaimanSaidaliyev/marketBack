from django.urls import path

from .views import *

urlpatterns = [
    path('mainpageinfo/', MainPageInfoView.as_view(),),
    path('mainpagesale/', MainPageSaleView.as_view(),),
]