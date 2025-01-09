from rest_framework import serializers
from .models import ReviewsShop


class ReviewsShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewsShop
        fields = ['user', 'description', 'created_at', 'grade', 'shop', 'telephone', 'photo']
        read_only_fields = ['created_at']
