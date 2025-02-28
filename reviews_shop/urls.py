from django.urls import path
from .views import ReviewsShopView, ReviewsShopByIdView

urlpatterns = [
    path('review/', ReviewsShopView.as_view()),
    path('review/<int:shop_id>/', ReviewsShopByIdView.as_view()),
]
