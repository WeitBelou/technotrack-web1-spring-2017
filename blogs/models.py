from django.conf import settings
from django.db import models


class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=255)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog')

    title = models.CharField(max_length=30)
    content = models.TextField()