from django.shortcuts import render
from rest_framework.views import APIView, Response
from reviews.models import *
from reviews.serializers import *


class ReviewsListAll(APIView):
    def get(self, request):
        reviews = Reviews.objects.filter(is_published=True).order_by('-created_at')
        count = reviews.count()
        reviews = reviews[0:5]
        return Response({
            'reviews': ReviewSerializer(reviews, many=True).data,
            'count': count
            }
        )