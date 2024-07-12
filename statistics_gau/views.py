from django.shortcuts import render
from rest_framework.views import APIView, Response
from statistics_gau.models import *
from statistics_gau.serializers import *
from products.models import Products
from rest_framework import status


class ProductStatisticsView(APIView):
    def get(self, request):
        product = ProductViewStatistics.objects.all()
        return Response(ProductStatisticsViewSerializer(product, many=True).data)

    def post(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')

        data = request.data.copy()
        data['client_ip'] = client_ip

        serializer = ProductStatisticsViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopStatisticsView(APIView):
    def get(self, request):
        shop = ShopViewStatistics.objects.all()
        return Response(ShopStatisticsViewSerializer(shop, many=True).data)

    def post(self, request, *args, **kwargs):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            client_ip = x_forwarded_for.split(',')[0]
        else:
            client_ip = request.META.get('REMOTE_ADDR')

        data = request.data.copy()
        data['client_ip'] = client_ip

        serializer = ShopStatisticsViewSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
