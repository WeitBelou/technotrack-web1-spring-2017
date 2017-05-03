from django.conf import settings
from django.db import models


class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    post = models.ForeignKey('blogs.Post', related_name='comments')

    text = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'Комментарий "{text}..." '.format(text=self.text[:40])

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ('created_at',)