# Generated by Django 4.2.10 on 2024-07-01 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0024_shop_instagram_login_shop_web_site_shop_youtube_src'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='tiktok_login',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Tiktok Логин'),
        ),
    ]