from django.contrib.auth.models import AbstractUser
from django.db import models

from upload_avatar.signals import avatar_crop_done
from upload_avatar.models import UploadAvatarMixIn


class User(AbstractUser, UploadAvatarMixIn):
    rating = models.IntegerField(verbose_name='Рейтинг', default=0)
    avatar_name = models.CharField(max_length=255)

    def get_uid(self):
        return self.user.id

    def get_avatar_name(self, size):
        return UploadAvatarMixIn.build_avatar_name(self, self.avatar_name, size)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-username',)


def save_avatar_in_db(sender, uid, avatar_name, **kwargs):
    if User.objects.filter(user_id=uid).exists():
        User.objects.filter(user_id=uid).update(avatar_name=avatar_name)
    else:
        User.objects.create(user_id=uid, avatar_name=avatar_name)


avatar_crop_done.connect(save_avatar_in_db)
