from rest_framework import serializers, generics
from .models import *
from django.db.models import Min


class ProductAllListSerializer(serializers.ModelSerializer):
    min_price = serializers.SerializerMethodField()

    def get_min_price(self, obj):
        return obj.product_product_price.aggregate(min_price=Min('price'))['min_price']

    class Meta:
        model = Products
        fields = ('__all__')
        depth = 2


class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')
        depth = 2


class ShopAllListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = ('__all__')


class ProductPriceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPrice
        fields = ('__all__')
        depth = 4


class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')
        depth = 2