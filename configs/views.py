from rest_framework.views import APIView, Response, status
from configs.serializers import *


class MainPageInfoView(APIView):
    def get(self, request):
        info = MainPageInfo.objects.first()
        return Response(MainPageInfoSerializer(info, many=False).data)


class MainPageSaleView(APIView):
    def get(self, request):
        info = MainPageSale.objects.all().order_by('?').first()
        return Response(MainPageSaleSerializer(info, many=False).data)