from rest_framework import serializers, generics
from statistics_gau.models import *


class ShopStatisticsViewSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = ShopViewStatistics
        fields = ('__all__')


class ProductStatisticsViewSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = ProductViewStatistics
        fields = ('__all__')