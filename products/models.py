from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


class Country(models.Model):
    title = models.CharField(max_length=99, verbose_name='Страна')
    coordinate_w = models.FloatField(default=0, blank=False, null=False, verbose_name='Ширина')
    coordinate_h = models.FloatField(default=0, blank=False, null=False, verbose_name='Долгота')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страна'
        ordering = ['-created_at']


class City(models.Model):
    title = models.CharField(max_length=99, verbose_name='Город')
    coordinate_w = models.FloatField(default=0, blank=False, null=False, verbose_name='Ширина')
    coordinate_h = models.FloatField(default=0, blank=False, null=False, verbose_name='Долгота')
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, verbose_name='Страна', related_name='city_country')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Город'
        ordering = ['-created_at']


class PremiumStatus(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название статуса')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Статус магазина'
        verbose_name_plural = 'Статус магазина'
        ordering = ['-created_at']


class Category(MPTTModel):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    class MPTTMeta:
        order_insertion_by = ['title']


class Products (models.Model):
    title = models.CharField(max_length=99, verbose_name='Название товара')
    description = models.TextField(max_length=500, verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='get_news')

    def my_func(self):
        return 'Hello from Model'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class Shop(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название магазина')
    description = models.TextField(max_length=500, verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    rating = models.FloatField(default=0, verbose_name='Рейтинг магазина')
    coordinate_w = models.FloatField(default=0, blank=False, null=False, verbose_name='Ширина')
    coordinate_h = models.FloatField(default=0, blank=False, null=False, verbose_name='Долгота')
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, verbose_name='Город', related_name='shop_city')
    address = models.CharField(max_length=2000, verbose_name='Адрес магазина')
    workTime = models.CharField(max_length=99, verbose_name='Режим работы магазина')
    phoneNumber = models.CharField(max_length=99, verbose_name='Телефон')
    premium_status = models.ForeignKey(PremiumStatus, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Статус магазина', related_name='get_shop_status')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Магазин'
        verbose_name_plural = 'Магазин'
        ordering = ['-created_at']


class ProductPrice(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, verbose_name='Магазин', related_name='shop_product_price')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, verbose_name='Товар', related_name='product_product_price')
    price = models.FloatField(default=0, verbose_name='Цена товара')
    new_price = models.FloatField(default=0, verbose_name='Новая цена на товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.shop.title + ' - ' + self.product.title + ' - ' + str(self.price)

    class Meta:
        verbose_name = 'Цены на товары'
        verbose_name_plural = 'Цены на товары'
        ordering = ['-created_at']


