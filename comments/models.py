from django.conf import settings
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('blogs.Post')