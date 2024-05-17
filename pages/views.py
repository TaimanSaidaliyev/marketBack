from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from pages.models import *
from pages.serializers import *


class PageViewBySlug(APIView):
    def get(self, request, slug):
        subscription_email = Page.objects.get(slug=slug)
        return Response(PageSerializer(subscription_email, many=False).data)