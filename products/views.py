from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *
from django.db.models import Q


class ProductAllListView(APIView):
    def get(self, request):
        products = Products.objects.all()
        return Response(
            {
            'products': ProductAllListSerializer(products, many=True).data
            }
        )


class ProductHozListView(APIView):
    def get(self, request):
        products = Products.objects.filter(category_id=7)
        return Response(
            {
            'products': ProductAllListSerializer(products, many=True).data
            }
        )


class ProductHealthListView(APIView):
    def get(self, request):
        products = Products.objects.filter(generalType=2)
        return Response(
            {
            'products': ProductAllListSerializer(products, many=True).data
            }
        )


class ProductByIdView(APIView):
    def get(self, request, product_id):
        product = Products.objects.get(pk=product_id)
        return Response(
            {
            'product': ProductDetailSerializer(product, many=False).data
            }
        )


class ShopSearchView(APIView):
    def post(self, request, field_text):
        if field_text == 'empty':
            shops = Shop.objects.all()
        else:
            shops = Shop.objects.filter(title__contains=field_text)
        return Response(
            {
                'shops': ShopAllListSerializer(shops, many=True).data
            }
        )


class ShopSingleView(APIView):
    def get(self, request, shop_id):
        shop = Shop.objects.get(pk=shop_id)
        return Response(
            {
                'shop': ShopAllListSerializer(shop, many=False).data
            }
        )


class ShopSearchProductView(APIView):
    def post(self, request, field_text):
        if field_text == 'empty':
            shops = Shop.objects.all()
        else:
            shops = Shop.objects.filter(title__contains=field_text)
        return Response(
            {
                'shops': ShopAllListSerializer(shops, many=True).data
            }
        )


class ShopAllListView(APIView):
    def post(self, request):
        try:
            shops = Shop.objects.filter(typeOfShop=request.GET["typeOfShop"])
        except:
            shops = Shop.objects.all()
        return Response(
            {
            'shops': ShopAllListSerializer(shops, many=True).data
            }
        )


class ProductsByShop(APIView):
    def get(self, request, shop_id):
        products = ProductPrice.objects.filter(shop_id=shop_id)
        return Response(
            {
                'list': ProductPriceSerializer(products, many=True).data
            }
        )


class ProductsByCategory(APIView):
    def get_products_in_category(self, category):
        products = Products.objects.filter(category__in=category.get_descendants(include_self=True))
        return products

    def get(self, request, category_id):
        category = Category.objects.get(pk=category_id)
        products = self.get_products_in_category(category)
        return Response(
            {
                'list': ProductAllListSerializer(products, many=True).data
            }
        )


class ProductsBySearch(APIView):
    def put(self, request):
        search_text = request.data.get('search_text')
        products = Products.objects.filter(Q(category__title__icontains=search_text) | Q(title__icontains=search_text))
        return Response(
            {
                'list': ProductAllListSerializer(products, many=True).data
            }
        )


class CategoryList(APIView):
    def get(self, request):
        categories = Category.objects.filter(level=0)
        return Response(
            {
                'categories': CategoryListSerializer(categories, many=True).data
            }
        )


class ShopsByProduct(APIView):
    def get(self, request, product_id):
        shops = ProductPrice.objects.filter(product_id=product_id).order_by('price')
        return Response({
            'shops': ProductPriceSerializer(shops, many=True).data
        })

# alembic
