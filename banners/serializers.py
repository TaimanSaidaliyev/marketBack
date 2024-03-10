from rest_framework import serializers, generics
from .models import *


class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ('__all__')
        depth = 2