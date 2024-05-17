from django.db import models


class MainPageInfo(models.Model):
    label_info_title = models.CharField(max_length=200, verbose_name='Название в блоке информации')
    label_info_desc = models.CharField(max_length=200, verbose_name='Описание в блоке информации')
    photo_info = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение большое', blank=True)

    label_info_1 = models.CharField(max_length=200, verbose_name='Напись первого блока')
    label_info_1_desc = models.CharField(max_length=200, verbose_name='Описание первого блока')
    photo_info_1 = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение первого блока', blank=True)

    label_info_2 = models.CharField(max_length=200, verbose_name='Напись второго блока')
    label_info_2_desc = models.CharField(max_length=200, verbose_name='Описание второго блока')
    photo_info_2 = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение второго блока', blank=True)

    label_info_3 = models.CharField(max_length=200, verbose_name='Напись третьего блока')
    label_info_3_desc = models.CharField(max_length=200, verbose_name='Описание третьего блока')
    photo_info_3 = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение третьего блока', blank=True)

    label_author = models.CharField(max_length=200, verbose_name='Автор')
    label_author_desc = models.CharField(max_length=200, verbose_name='Описание автора')
    photo_author = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение автора', blank=True)

    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата изменения')

    def __str__(self):
        return self.label_info_title

    class Meta:
        verbose_name = 'Блок на главной странице'
        verbose_name_plural = 'Блок на главной странице'


class MainPageSale(models.Model):
    subtitle = models.CharField(max_length=200, verbose_name='Подпись')
    title = models.CharField(max_length=200, verbose_name='Надпись')
    description = models.CharField(max_length=500, verbose_name='Описание')
    button_label = models.CharField(max_length=20, verbose_name='Текст кнопки')
    link = models.CharField(max_length=500, verbose_name='Ссылка')
    photo = models.ImageField(upload_to='other/mainpage/%Y/%m/%d', verbose_name='Изображение на фон', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Акция на главной странице'
        verbose_name_plural = 'Акция на главной странице'