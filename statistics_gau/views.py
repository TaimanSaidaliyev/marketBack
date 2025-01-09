from django.shortcuts import render
from rest_framework.views import APIView, Response
from statistics_gau.models import *
from statistics_gau.serializers import *
from products.models import Products
from rest_framework import status
from rest_framework.response import Response
from django.db.models import Count
from django.db.models.functions import ExtractMonth, ExtractYear
import requests


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

        serializer = ProductStatisticsPostSerializer(data=data)
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

        serializer = ShopStatisticsPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ShopStatisticsByPeriodAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = (
            ShopViewStatistics.objects.annotate(
                year=ExtractYear('created_at'),
                month=ExtractMonth('created_at')
            )
            .values('year', 'month')
            .annotate(count=Count('id'))
            .order_by('year', 'month')
        )
        return Response(data)


class ShopStatisticsByRegionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        # Получение всех записей с регионами, собранными из IP
        statistics = ShopViewStatistics.objects.values('client_ip').annotate(count=Count('id'))
        region_data = []

        for stat in statistics:
            client_ip = stat['client_ip']
            try:
                # Определяем регион для каждого IP через ip-api
                response = requests.get(f'http://ip-api.com/json/{client_ip}')
                geo_data = response.json()

                if geo_data['status'] == 'success':
                    region_name = geo_data.get('regionName', 'Неизвестный регион')
                    region_data.append({'region': region_name, 'count': stat['count']})
                else:
                    region_data.append({'region': 'Неизвестный регион', 'count': stat['count']})
            except Exception as e:
                region_data.append({'region': 'Ошибка определения региона', 'count': stat['count']})

        # Группируем данные по регионам
        grouped_data = {}
        for item in region_data:
            region = item['region']
            grouped_data[region] = grouped_data.get(region, 0) + item['count']

        # Формируем ответ
        result = [{'region': region, 'count': count} for region, count in grouped_data.items()]
        return Response(result)


class ProductStatisticsByPeriodAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = (
            ProductViewStatistics.objects.annotate(
                year=ExtractYear('created_at'),
                month=ExtractMonth('created_at')
            )
            .values('year', 'month')
            .annotate(count=Count('id'))
            .order_by('year', 'month')
        )
        return Response(data)


class ProductStatisticsByRegionAPIView(APIView):
    def get(self, request, *args, **kwargs):
        data = (
            ProductViewStatistics.objects.values('region')
            .annotate(count=Count('id'))
            .order_by('-count')
        )
        return Response(data)


class SingleShopStatisticsByPeriodAPIView(APIView):
    def get(self, request, shop_id, *args, **kwargs):
        data = (
            ShopViewStatistics.objects.filter(shop_id=shop_id)
            .annotate(
                year=ExtractYear('created_at'),
                month=ExtractMonth('created_at')
            )
            .values('year', 'month')
            .annotate(count=Count('id'))
            .order_by('year', 'month')
        )
        return Response(data)


class SingleProductStatisticsByPeriodAPIView(APIView):
    def get(self, request, product_id, *args, **kwargs):
        data = (
            ProductViewStatistics.objects.filter(product_id=product_id)
            .annotate(
                year=ExtractYear('created_at'),
                month=ExtractMonth('created_at')
            )
            .values('year', 'month')
            .annotate(count=Count('id'))
            .order_by('year', 'month')
        )
        return Response(data)
