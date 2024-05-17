from django.db import models


class SubscriptionEmail(models.Model):
    email = models.CharField(max_length=99, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return f"{self.email}"

    class Meta:
        verbose_name = 'Подписки Email'
        verbose_name_plural = 'Подписки Email'
        ordering = ['-created_at']