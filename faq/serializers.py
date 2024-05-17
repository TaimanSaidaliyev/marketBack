from rest_framework import serializers, generics
from faq.models import *


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = ('__all__')
        depth = 2


class FAQContactFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = FaqContactForm
        fields = ('__all__')