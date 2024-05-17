# Generated by Django 4.2.10 on 2024-05-03 11:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FaqContactForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=300, verbose_name='Почта')),
                ('fio', models.CharField(max_length=300, verbose_name='ФИО')),
                ('question', models.TextField(max_length=500, verbose_name='Вопрос')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Дата изменения')),
            ],
            options={
                'verbose_name': 'FAQ Контактная форма',
                'verbose_name_plural': 'FAQ Контактная форма',
                'ordering': ['-created_at'],
            },
        ),
    ]
