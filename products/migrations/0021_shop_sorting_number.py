# Generated by Django 4.2.10 on 2024-05-04 09:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0020_alter_category_common_type_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='sorting_number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Порядок сортировки'),
        ),
    ]