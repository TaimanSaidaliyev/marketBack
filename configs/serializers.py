from rest_framework import serializers, generics
from configs.models import *


class MainPageInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageInfo
        fields = ('__all__')
        depth = 2


class MainPageSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainPageSale
        fields = ('__all__')
        depth = 2