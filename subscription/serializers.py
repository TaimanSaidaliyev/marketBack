from rest_framework import serializers, generics
from subscription.models import *


class SubscriptionEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubscriptionEmail
        fields = ('__all__')