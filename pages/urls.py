from django.urls import path

from .views import *

urlpatterns = [
    path('<str:slug>/', PageViewBySlug.as_view(),),
]