from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.models import CloudinaryField


class User(AbstractUser):
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    avatar = CloudinaryField(verbose_name='Аватар')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-username',)
