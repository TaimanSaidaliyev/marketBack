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
    zoom = models.IntegerField(blank=True, default=12, verbose_name='Зум')

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


class CommonTypeOfCategory(models.Model):
    slug = title = models.CharField(max_length=100, unique=True, db_index=True, verbose_name='slug')
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группировка категорий'
        verbose_name_plural = 'Группировка категорий'
        ordering = ['title']


class Category(MPTTModel):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Категории')
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    common_type_category = models.ForeignKey(CommonTypeOfCategory, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Группировка категорий', related_name='get_common_category')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    class MPTTMeta:
        order_insertion_by = ['title']


class GeneralCategoriesOfProduct(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Общая категория товара')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общая категория товара'
        verbose_name_plural = 'Общая категория товара'
        ordering = ['title']


class Products (models.Model):
    title = models.CharField(max_length=99, verbose_name='Название товара')
    description = models.TextField(max_length=500, verbose_name='Описание товара')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name='Категория', related_name='get_news')
    generalType = models.ManyToManyField(GeneralCategoriesOfProduct, blank=True, verbose_name='Общие категории',
                                         related_name='get_general_type_of_shop')
    show_calories = models.BooleanField(default=False, verbose_name='Показывать БЖУ')
    protein = models.FloatField(default=0, null=True, verbose_name='Белки')
    carbs = models.FloatField(default=0, null=True, verbose_name='Углеводы')
    fat = models.FloatField(default=0, null=True, verbose_name='Жир')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Товары'
        verbose_name_plural = 'Товары'
        ordering = ['-created_at']


class DeliveryType(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Вид доставки')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вид доставки'
        verbose_name_plural = 'Вид доставки'
        ordering = ['title']


class TypeOfShop(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Тип тороговой точки')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип торговой точки'
        verbose_name_plural = 'Тип торговой точки'
        ordering = ['title']


class GeneralCategories(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Общая категория торговой точки')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Общая категория торговой точки'
        verbose_name_plural = 'Общая категория торговой точки'
        ordering = ['title']


class AdditionalAttributes(models.Model):
    title = models.CharField(max_length=100, db_index=True, verbose_name='Название атрибута')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Дополнительные атрибуты'
        verbose_name_plural = 'Дополнительные атрибуты'
        ordering = ['title']


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
    address = models.CharField(blank=True, null=True, max_length=2000, verbose_name='Адрес магазина')
    workTime = models.CharField(max_length=99, verbose_name='Режим работы магазина')
    phoneNumber = models.CharField(max_length=99, verbose_name='Телефон')
    instagram_login = models.CharField(blank=True, null=True, max_length=50, verbose_name='Instagram Логин')
    tiktok_login = models.CharField(blank=True, null=True, max_length=50, verbose_name='Tiktok Логин')
    web_site = models.CharField(blank=True, null=True, max_length=200, verbose_name='Ссылка на сайт')
    premium_status = models.ForeignKey(PremiumStatus, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Статус магазина', related_name='get_shop_status')
    typeOfShop = models.ForeignKey(TypeOfShop, on_delete=models.PROTECT, blank=True, null=True, verbose_name='Тип торговой точки', related_name='get_type_of_shop')
    generalType = models.ManyToManyField(GeneralCategories, blank=True, verbose_name='Общие категории', related_name='get_general_type_of_shop')
    deliveryType = models.ManyToManyField(DeliveryType, blank=True, verbose_name='Методы доставки', related_name='get_delivery_type_of_shop')
    additionalAttributes = models.ManyToManyField(AdditionalAttributes, blank=True, verbose_name='Дополнительные атрибуты', related_name='get_additional_attributes_of_shop')
    sorting_number = models.IntegerField(blank=True, null=True, verbose_name='Порядок сортировки')
    youtube_src = models.CharField(blank=True, null=True, max_length=1000, verbose_name='Ссылка на Youtube')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Торговая точка'
        verbose_name_plural = 'Торговая точка'
        ordering = ['-created_at']


class ShopImage(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='shop_images/%Y/%m/%d', verbose_name='Изображение')
    description = models.CharField(max_length=255, blank=True, verbose_name='Описание')

    def __str__(self):
        return f"Image for {self.shop.title}"

    class Meta:
        verbose_name = 'Изображение магазина'
        verbose_name_plural = 'Изображения магазина'


class ProductPrice(models.Model):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, verbose_name='Магазин', related_name='shop_product_price')
    product = models.ForeignKey(Products, on_delete=models.CASCADE, blank=True, verbose_name='Товар', related_name='product_product_price')
    price = models.FloatField(default=0, verbose_name='Цена товара')
    new_price = models.FloatField(default=0, verbose_name='Старая цена на товар')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.shop.title + ' - ' + self.product.title + ' - ' + str(self.price)

    class Meta:
        verbose_name = 'Цены на товары'
        verbose_name_plural = 'Цены на товары'
        ordering = ['-created_at']

