from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from PIL import Image
from io import BytesIO
from django.core.files.base import ContentFile


class Reviews(models.Model):
    user = models.CharField(max_length=99, verbose_name='ФИО')
    label = models.CharField(default='', max_length=99, verbose_name='Надпись')
    description = models.TextField(max_length=500, verbose_name='Отзыв')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    grade = models.IntegerField(default=5, validators=[MaxValueValidator(5), MinValueValidator(1)], verbose_name='Оценка')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', verbose_name='Изображение', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def save(self, *args, **kwargs):
        if self.photo and not self.photo._committed:
            img = Image.open(self.photo)

            img = img.resize((250, 250), Image.Resampling.LANCZOS)

            output = BytesIO()
            img.save(output, format='JPEG', quality=100)
            output.seek(0)

            self.photo.save(
                self.photo.name,
                ContentFile(output.read()),
                save=False
            )
            output.close()

        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.user} - {self.description[:20]} - {self.grade}"

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-created_at']
