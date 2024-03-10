from django.db import models


class Banners(models.Model):
    title = models.CharField(max_length=99, verbose_name='Название баннера')
    link = models.CharField(max_length=300, verbose_name='Ссылка')
    photo = models.ImageField(upload_to='banners/%Y/%m/%d', verbose_name='Изображение', blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Баннеры на главной странице'
        verbose_name_plural = 'Баннеры на главной странице'
        ordering = ['-created_at']