# Generated by Django 4.2.10 on 2025-02-04 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews_shop', '0003_reviewsshop_photo_reviewsshop_telephone_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsshop',
            name='is_published',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Опубликовано'),
        ),
    ]
