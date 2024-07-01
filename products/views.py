from django.shortcuts import render
from rest_framework.views import APIView, Response
from .models import *
from .serializers import *
from django.db.models import Q
from django.shortcuts import get_object_or_404
from utils.distance import *


class ProductAllListView(APIView):
    def get(self, request):
        shops_ids = request.query_params.get('shops_ids')
        categories_ids = request.query_params.get('categories_ids')
        common_category = request.query_params.get('common_category')
        product_general_types_ids = request.query_params.get('product_general_types_ids')
        max_price = request.query_params.get('max_price')
        min_price = request.query_params.get('min_price')
        search = request.query_params.get('search')
        count_on_page = request.query_params.get('count_on_page', 10)
        page_number = request.query_params.get('page_number', 1)
        city = request.query_params.get('city')
        products = Products.objects.all()

        try:
            if search or len(search) > 2:
                products = products.filter(Q(title__icontains=search) | Q(description__icontains=search) | Q(category__title__icontains=search) | Q(generalType__title__icontains=search))
        except:
            None

        if shops_ids:
            shops_ids = [int(id) for id in shops_ids.split(',')]
            products = products.filter(product_product_price__shop__id__in=shops_ids)

        if categories_ids:
            categories_ids = [int(id) for id in categories_ids.split(',')]
            products = products.filter(category_id__in=categories_ids)

        if common_category:
            products = products.filter(category__common_type_category__slug=common_category)

        if product_general_types_ids:
            product_general_types_ids = [int(id) for id in product_general_types_ids.split(',')]
            products = products.filter(generalType__in=product_general_types_ids)

        if max_price:
            products = products.filter(product_product_price__price__lte=max_price)

        if min_price:
            products = products.filter(product_product_price__price__gte=min_price)

        if city:
            products = products.filter(product_product_price__shop__city_id=city)

        products = products.distinct()
        items_count = products.count()
        products = products[0 + (int(page_number) - 1)*count_on_page:int(page_number) * count_on_page]
        serializer = ProductAllListSerializer(products, many=True)
        return Response({'products': serializer.data, 'count': items_count})


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
            shops = Shop.objects.filter(title__icontains=field_text)
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
    def get(self, request):
        city = request.query_params.get('city')
        types_of_shops = request.query_params.get('typesOfShops')
        delivery_types = request.query_params.get('deliveryTypes')
        general_categories = request.query_params.get('generalCategories')
        page_number = request.query_params.get('pageNumber', 1)
        count_on_page = request.query_params.get('count_on_page', 12)
        sort_by = request.query_params.get('sortBy')
        coordinate_w_t = float(request.query_params.get('coordinate_w_t', 0))
        coordinate_h_t = float(request.query_params.get('coordinate_h_t', 0))

        shops = Shop.objects.all().order_by('-sorting_number')

        if types_of_shops:
            type_ids = [int(id) for id in types_of_shops.split(',')]
            shops = shops.filter(typeOfShop__in=type_ids).distinct()

        if delivery_types:
            delivery_ids = [int(id) for id in delivery_types.split(',')]
            shops = shops.filter(deliveryType__in=delivery_ids).distinct()

        if general_categories:
            gen_cat = [int(id) for id in general_categories.split(',')]
            shops = shops.filter(generalType__in=gen_cat).distinct()

        if city:
            shops = shops.filter(city=city)

        if sort_by:
            if(sort_by == 'asc'):
                shops = shops.order_by('-pk')
            if(sort_by == 'desc'):
                shops = shops.order_by('pk')
            if(sort_by == 'alph_a_b'):
                shops = shops.order_by('title')
            if(sort_by == 'alph_b_a'):
                shops = shops.order_by('-title')
            if(sort_by == 'default'):
                shops = shops.order_by('-sorting_number')

        items_count = shops.count()

        shops = shops[0 + (int(page_number) - 1) * count_on_page:int(page_number) * count_on_page]

        serializer = ShopAllListSerializer(shops, many=True)

        shops_with_distance = []

        for shop, shop_data in zip(shops, serializer.data):
            distance = geodesic((coordinate_w_t, coordinate_h_t), (shop.coordinate_w, shop.coordinate_h)).meters
            if coordinate_w_t > 0 and coordinate_h_t > 0:
                shop_data['distance'] = distance
            shops_with_distance.append(shop_data)

        if sort_by:
            if sort_by == 'distance':
                shops_with_distance.sort(key=lambda x: x['distance'])

        return Response(
            {
                'shops': shops_with_distance,
                'count': items_count,
            }
        )


class ProductsByShop(APIView):
    def get(self, request, shop_id):
        products = ProductPrice.objects.filter(shop_id=shop_id)
        count = products.count()
        return Response(
            {
                'products': ProductPriceSerializer(products, many=True).data
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
        products = Products.objects.filter(Q(category__title__icontains=search_text) | Q(title__icontains=search_text)
                                           | Q(category__title__icontains=search_text) | Q(generalType__title__icontains=search_text))
        return Response(
            {
                'list': ProductAllListSerializer(products, many=True).data
            }
        )


class CategoryList(APIView):
    def get(self, request):
        common_category = request.query_params.get('common_category')

        categories = Category.objects.filter(level=0)

        if common_category:
            categories = categories.filter(common_type_category__slug=common_category)

        return Response(
            {
                'categories': CategoryListSerializer(categories, many=True).data
            }
        )


class ShopsByProduct(APIView):
    def get(self, request, product_id):
        city = request.query_params.get('city')
        shops = ProductPrice.objects.filter(product_id=product_id).order_by('price')

        if city:
            shops = shops.filter(shop__city=city)

        return Response({
            'shops': ProductPriceSerializer(shops, many=True).data
        })


class ProductGeneralTypeList(APIView):
    def get(self, request):
        types = GeneralCategoriesOfProduct.objects.all()
        return Response({
            'types': ProductGeneralTypeListSerializer(types, many=True).data
        })


class CitiesList(APIView):
    def get(self, request):
        cities = City.objects.all().order_by('title')
        return Response({
            'cities': CitiesListSerializer(cities, many=True).data
        })


class ShopAttributesDict(APIView):
    def get(self, request):
        delivery_types = DeliveryType.objects.all()
        services = AdditionalAttributes.objects.all()
        general_categories = GeneralCategories.objects.all()
        type_of_shop = TypeOfShop.objects.all()
        premium_status = PremiumStatus.objects.all()

        return Response({
            'delivery_types': DeliveryTypeSerializer(delivery_types, many=True).data,
            'services': AdditionalAttributesSerializer(services, many=True).data,
            'general_categories': GeneralCategoriesSerializer(general_categories, many=True).data,
            'type_of_shop': TypeOfShopSerializer(type_of_shop, many=True).data,
            'premium_status': PremiumStatusSerializer(premium_status, many=True).data,
        })


class RecentlyViewed(APIView):
    def put(self, request):
        get_data = request.data
        list_v = []
        for item in get_data:
            try:
                item_type = item['type']
                item_id = item['id']
                if item_type == 'shop':
                    shop = get_object_or_404(Shop, pk=item_id)
                    photo_url = shop.photo.url if shop.photo else ''
                    list_v.append({
                        'id': shop.id,
                        'title': shop.title,
                        'photo': photo_url,
                        'type': 'shop',
                        'category': shop.typeOfShop.title
                    })
                elif item_type == 'product':
                    product = get_object_or_404(Products, pk=item_id)
                    photo_url = product.photo.url if product.photo else ''
                    list_v.append({
                        'id': product.id,
                        'title': product.title,
                        'photo': photo_url,
                        'type': 'product',
                        'category': product.category.title
                    })
            except:
                None
        return Response(list_v)



class MightInterestedProducts(APIView):
    def get(self, request):
        products = Products.objects.order_by('?')[:20]
        return Response(
            {
            'products': ProductAllListSerializer(products, many=True).data
            }
        )


class CommonTypeOfCategoryDict(APIView):
    def get(self, request):
        list = CommonTypeOfCategory.objects.all()
        return Response(
            CommonTypeOfCategorySerializer(list, many=True).data
        )


class DeliveryTypeDict(APIView):
    def get(self, request):
        deliveryTypes = DeliveryType.objects.all()
        return Response(
            DeliveryTypeSerializer(deliveryTypes, many=True).data
        )


class GeneralCategoriesDict(APIView):
    def get(self, request):
        generalCategories = GeneralCategories.objects.all()
        return Response(
            GeneralCategoriesSerializer(generalCategories, many=True).data
        )