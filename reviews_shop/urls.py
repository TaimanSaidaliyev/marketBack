from django.urls import path
from .views import ReviewsShopView

urlpatterns = [
    path('review/', ReviewsShopView.as_view()),
]
