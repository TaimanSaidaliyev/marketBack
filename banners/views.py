from django.shortcuts import render
from .models import *
from rest_framework.views import APIView, Response
from .serializers import *


class BannersList(APIView):
    def get(self, request):
        banners = Banners.objects.all()
        return Response(
            {
                'banners': BannersSerializer(banners, many=True).data
            }
        )