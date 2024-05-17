from django.urls import path

from .views import *

urlpatterns = [
    path('add/', SubscriptionEmailListAll.as_view(),),
]