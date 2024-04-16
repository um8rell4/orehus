from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class OrehusChange(models.Model):
    comment = models.CharField(verbose_name='Комментарий', max_length=300, blank=True)
    operation = models.IntegerField(verbose_name='Сколько прибавляем?')
    datetime_comment = models.DateTimeField(verbose_name='Время комментария', auto_now_add=True)
    orehus_user = models.ForeignKey('CustomUser', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Кому '
                                                                                                      'прибавляем?')
    rating_was = models.IntegerField(verbose_name='Сколько было', null=True)
    rating_new = models.IntegerField(verbose_name='Сколько стало', null=True)
    who_changed = models.CharField(verbose_name='Кто прибавляет?', max_length=20)

    def get_absolute_url(self):
        return reverse('user_profile', kwargs={"profile_id": self.pk})

    class Meta:
        verbose_name = 'Изменение рейтинга'
        verbose_name_plural = 'Изменение рейтинга'
        ordering = ['-datetime_comment']


class CustomUser(AbstractUser):
    unchanged_name = models.TextField(verbose_name='Неизменяемое имя', max_length=20)
    bio = models.TextField(verbose_name='Обо мне', max_length=300, blank=True)
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    birth_date = models.DateField(blank=True, )
    user_vk_url = models.URLField(blank=True, null=True)
    user_img = models.ImageField(upload_to='photos/%Y/%m/%d/', verbose_name='Фото', blank=True, null=True)
    user_zodiac = models.ForeignKey('UserZodiacSign', on_delete=models.PROTECT, verbose_name='Знак зодиака', null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['-rating']

    def __str__(self):
        return self.unchanged_name


class UserZodiacSign(models.Model):
    user_zodiac_sign_img = models.ImageField(upload_to='zodiac_sign/', verbose_name='Иконка', blank=True,
                                             null=True)
    zodiac_sign = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Знак зодиака'

    def __str__(self):
        return self.zodiac_sign
