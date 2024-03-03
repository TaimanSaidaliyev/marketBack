# Generated by Django 4.2.10 on 2024-03-01 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_shop_alter_products_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='coordinate_h',
            field=models.FloatField(default=0, verbose_name='Долгота'),
        ),
        migrations.AddField(
            model_name='shop',
            name='coordinate_w',
            field=models.FloatField(default=0, verbose_name='Ширина'),
        ),
        migrations.AddField(
            model_name='shop',
            name='products',
            field=models.ManyToManyField(blank=True, null=True, related_name='shop_products', to='products.products', verbose_name='Товары магазина'),
        ),
    ]
