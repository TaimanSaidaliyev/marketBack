from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin


class ShopImageInline(admin.TabularInline):
    model = ShopImage
    extra = 1


class ShopAdmin(admin.ModelAdmin):
    inlines = [ShopImageInline]


class ProductsAdmin(admin.ModelAdmin):
    search_fields = ['title', 'description']  # Поля, по которым будет производиться поиск

admin.site.register(Products, ProductsAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(ProductPrice)
admin.site.register(PremiumStatus)
admin.site.register(Category, MPTTModelAdmin)
admin.site.register(GeneralCategories)
admin.site.register(TypeOfShop)
admin.site.register(DeliveryType)
admin.site.register(GeneralCategoriesOfProduct)
admin.site.register(AdditionalAttributes)
admin.site.register(CommonTypeOfCategory)
admin.site.register(SpecialMenu)