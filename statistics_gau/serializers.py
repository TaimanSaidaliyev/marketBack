from rest_framework import serializers, generics
from statistics_gau.models import *


class ShopStatisticsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopViewStatistics
        fields = ('__all__')


class ProductStatisticsPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewStatistics
        fields = ('__all__')


class ShopStatisticsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopViewStatistics
        fields = ('__all__')


class ProductStatisticsViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductViewStatistics
        fields = ('__all__')