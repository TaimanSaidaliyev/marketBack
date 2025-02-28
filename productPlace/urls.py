from django.contrib import admin
from django.urls import path, include
from products.views import *
from banners.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/list/all/', ProductAllListView.as_view()),
    path('products/mightbeinterested/', MightInterestedProducts.as_view()),
    path('products/list/hoz/', ProductHozListView.as_view()),
    path('products/list/health/', ProductHealthListView.as_view()),
    path('products/detail/<int:product_id>/', ProductByIdView.as_view()),
    path('shops/list/', ShopAllListView.as_view()),
    path('shops/deliverytype/dict/', DeliveryTypeDict.as_view()),
    path('shops/general_categories/dict/', GeneralCategoriesDict.as_view()),
    path('shops/list/<str:field_text>', ShopSearchView.as_view()),
    path('products/search/', ProductsBySearch.as_view()),
    path('shops/product/list/<str:field_text>', ShopSearchProductView.as_view()),
    path('shop/<int:shop_id>/', ShopSingleView.as_view()),
    path('shop/<int:shop_id>/products/', ProductsByShop.as_view()),
    path('category/list/', CategoryList.as_view()),
    path('category/<int:category_id>/products/', ProductsByCategory.as_view()),
    path('shops/<int:product_id>/products/', ShopsByProduct.as_view()),
    path('banners/list/', BannersList.as_view()),
    path('banners/detail/<int:banner_id>/', BannerDetail.as_view()),
    path('product_general_types/list/', ProductGeneralTypeList.as_view()),
    path('cities/list/', CitiesList.as_view()),
    path('shop/dict/', ShopAttributesDict.as_view()),
    path('recently/', RecentlyViewed.as_view()),
    path('common_category/dict/', CommonTypeOfCategoryDict.as_view()),
    path('special_menu/<int:shop_id>/', SpecialMenuApiView.as_view()),
    path('special_menu/', SpecialMenuApiView.as_view()),
    path('reviews/', include('reviews.urls')),
    path('faq/', include('faq.urls')),
    path('subscription/', include('subscription.urls')),
    path('page/', include('pages.urls')),
    path('configs/', include('configs.urls')),
    path('statistics/', include('statistics_gau.urls')),
    path('reviews_shop/', include('reviews_shop.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
