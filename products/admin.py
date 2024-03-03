from django.contrib import admin
from .models import *
from mptt.admin import MPTTModelAdmin

admin.site.register(Products)
admin.site.register(Shop)
admin.site.register(City)
admin.site.register(Country)
admin.site.register(ProductPrice)
admin.site.register(PremiumStatus)
admin.site.register(Category, MPTTModelAdmin)