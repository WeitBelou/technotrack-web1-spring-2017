from django.conf import settings
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog')
