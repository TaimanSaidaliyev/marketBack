from rest_framework.views import APIView, Response
from .serializers import *


class BannersList(APIView):
    def get(self, request):
        banners = Banners.objects.all()
        city = request.query_params.get('city')

        if city:
            banners = banners.filter(city=city)
        return Response(
            {
                'banners': BannersSerializer(banners, many=True).data
            }
        )


class BannerDetail(APIView):
    def get(self, request, banner_id):
        banner = Banners.objects.get(pk=banner_id)
        return Response({
            'banner': BannersSerializer(banner, many=False).data
        })

