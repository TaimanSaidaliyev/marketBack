# Generated by Django 4.2.10 on 2024-03-01 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_products_address_alter_shop_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='address',
        ),
        migrations.AddField(
            model_name='shop',
            name='address',
            field=models.CharField(default=1, max_length=2000, verbose_name='Адрес магазина'),
            preserve_default=False,
        ),
    ]
