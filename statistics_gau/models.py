from django.db import models
from products.models import Shop, Products


class ShopViewStatistics(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, verbose_name='Торговая точка', related_name='shop_statistics')
    client_ip = models.CharField(max_length=100, db_index=True, verbose_name='IP клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return self.shop.title

    class Meta:
        verbose_name = 'Статистика по ресторану'
        verbose_name_plural = 'Статистика по ресторану'
        ordering = ['shop']


class ProductViewStatistics(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, verbose_name='Продукт', related_name='product_statistics')
    client_ip = models.CharField(max_length=100, db_index=True, verbose_name='IP клиента')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата просмотра')

    def __str__(self):
        return self.product.title

    class Meta:
        verbose_name = 'Статистика по продуктам'
        verbose_name_plural = 'Статистика по продуктам'
        ordering = ['product']


