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
    min_price = serializers.SerializerMethodField()

    def get_min_price(self, obj):
        return obj.product_product_price.aggregate(min_price=Min('price'))['min_price']

    class Meta:
        model = Products
        fields = ('__all__')
        depth = 2


class ShopImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShopImage
        fields = ('id', 'image', 'description')


class ShopAllListSerializer(serializers.ModelSerializer):
    images = ShopImageSerializer(many=True, read_only=True)

    class Meta:
        model = Shop
        fields = ('__all__')
        depth = 2


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


class ProductGeneralTypeListSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCategoriesOfProduct
        fields = ('__all__')
        depth = 2


class CitiesListSerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ('__all__')
        depth = 2


class DeliveryTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = DeliveryType
        fields = ('__all__')
        depth = 2


class AdditionalAttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalAttributes
        fields = ('__all__')
        depth = 2


class GeneralCategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralCategories
        fields = ('__all__')
        depth = 2


class TypeOfShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = TypeOfShop
        fields = ('__all__')
        depth = 2


class PremiumStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = PremiumStatus
        fields = ('__all__')
        depth = 2


class CommonTypeOfCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CommonTypeOfCategory
        fields = ('__all__')
        depth = 2


class SpecialMenuSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpecialMenu
        fields = ('__all__')