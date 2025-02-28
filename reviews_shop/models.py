from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from products.models import Shop


class ReviewsShop(models.Model):
    user = models.CharField(max_length=99, blank=True, null=True, verbose_name='ФИО')
    description = models.TextField(max_length=500, blank=True, null=True, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    grade = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name='Оценка')
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE, blank=True, verbose_name='Торговая точка',
                             related_name='shop_reviews')
    telephone = models.CharField(max_length=99, blank=True, null=True, verbose_name='Номер телефона')
    photo = models.ImageField(upload_to='photos/reviews_shop/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=False, blank=True, null=True, verbose_name='Опубликовано')

    def __str__(self):
        return f"{self.shop.title} - {self.user} - {self.description[:20]} - {self.grade}"

    class Meta:
        verbose_name = 'Отзывы по торговым точкам'
        verbose_name_plural = 'Отзывы по торговым точкам'
        ordering = ['-created_at']