from django.urls import path

from .views import *

urlpatterns = [
    path('list/', ReviewsListAll.as_view(),),
]