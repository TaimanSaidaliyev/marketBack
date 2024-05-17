from rest_framework import serializers, generics
from reviews.models import *


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reviews
        fields = ('__all__')
        depth = 2