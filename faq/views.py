from django.shortcuts import render
from faq.models import *
from rest_framework.views import APIView, Response, status
from faq.serializers import *


class FAQList(APIView):
    def get(self, request):
        faq = FAQ.objects.filter(is_published=True).order_by('-created_at')
        return Response(FAQSerializer(faq, many=True).data)


class FAQContactForm(APIView):
    def post(self, request):
        serializer = FAQContactFormSerializer(data=request.data)
        print(request.data)
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