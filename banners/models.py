from django.db import models
from products.models import Shop
from products.models import City


class Banners(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название акции')
    description = models.CharField(max_length=1000, verbose_name='Описание')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Магазин', related_name='shop_banner')
    link = models.CharField(max_length=300, verbose_name='Ссылка')
    photo = models.ImageField(upload_to='banners/%Y/%m/%d', verbose_name='Изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Город', related_name='banner_city')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннеры на главной странице'
        verbose_name_plural = 'Баннеры на главной странице'
        ordering = ['-created_at']