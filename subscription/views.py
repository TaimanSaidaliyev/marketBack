from django.shortcuts import render
from rest_framework.views import APIView, Response, status
from subscription.models import *
from subscription.serializers import *


class SubscriptionEmailListAll(APIView):
    def get(self, request):
        subscription_email = SubscriptionEmail.objects.filter(is_published=True).order_by('-created_at')
        return Response(SubscriptionEmailSerializer(subscription_email, many=True).data)

    def post(self, request):
        serializer = SubscriptionEmailSerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response({
                    'status': 'Успешно добавлено'
                }, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({
                    'status': 'Добавление невозможно',
                    'error': str(e)
                }, status=status.HTTP_400_BAD_REQUEST)
        return Response({
            'status': 'Добавление невозможно',
        }, status=status.HTTP_400_BAD_REQUEST)