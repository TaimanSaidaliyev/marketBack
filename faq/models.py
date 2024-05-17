from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=99, verbose_name='Вопрос')
    answer = models.TextField(max_length=500, verbose_name='Ответ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'FAQ'
        verbose_name_plural = 'FAQ'
        ordering = ['-created_at']


class FaqContactForm(models.Model):
    email = models.CharField(max_length=300, verbose_name='Почта')
    fio = models.CharField(max_length=300, verbose_name='ФИО')
    question = models.TextField(max_length=500, verbose_name='Вопрос')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.question}"

    class Meta:
        verbose_name = 'FAQ Контактная форма'
        verbose_name_plural = 'FAQ Контактная форма'
        ordering = ['-created_at']
