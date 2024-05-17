from rest_framework import serializers, generics
from .models import *


class PageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Page
        fields = ('__all__')
        depth = 4