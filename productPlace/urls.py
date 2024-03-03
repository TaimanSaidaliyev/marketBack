from django.contrib import admin
from django.urls import path
from products.views import *
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/list/all/', ProductAllListView.as_view()),
    path('products/detail/<int:product_id>/', ProductByIdView.as_view()),
    path('shops/list/', ShopAllListView.as_view()),
    path('shops/list/<str:field_text>', ShopSearchView.as_view()),
    path('products/search/', ProductsBySearch.as_view()),
    path('shops/product/list/<str:field_text>', ShopSearchProductView.as_view()),
    path('shop/<int:shop_id>', ShopSingleView.as_view()),
    path('shop/<int:shop_id>/products/', ProductsByShop.as_view()),
    path('category/list/', CategoryList.as_view()),
    path('category/<int:category_id>/products/', ProductsByCategory.as_view()),
    path('shops/<int:product_id>/products/', ShopsByProduct.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
