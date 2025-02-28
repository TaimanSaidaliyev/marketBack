from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ReviewsShopSerializer
from .models import ReviewsShop


class ReviewsShopView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = ReviewsShopSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewsShopByIdView(APIView):
    def get(self, request, shop_id):
        try:
            reviews = ReviewsShop.objects.filter(shop_id=shop_id, is_published=True)
            return Response(ReviewsShopSerializer(reviews, many=True).data, status=status.HTTP_201_CREATED)
        except:
            return Response('Reviews not found', status=status.HTTP_400_BAD_REQUEST)
