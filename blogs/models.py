from django.conf import settings
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{name}'.format(id=self.id, name=self.name)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ('-created_at',)


class BlogQuerySet(models.QuerySet):

    def optimized(self):
        qs = self.select_related('owner')
        qs = qs.select_related('blog')
        qs = qs.prefetch_related('categories')
        return qs

class Blog(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='blogs')

    title = models.CharField(max_length=255)
    description = models.TextField()
    categories = models.ManyToManyField('Category', related_name='categories')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = BlogQuerySet.as_manager()

    def __str__(self):
        return '{title}'.format(title=self.title)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ('-created_at',)


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    blog = models.ForeignKey('blogs.Blog', related_name='posts')

    title = models.CharField(max_length=255)
    content = models.TextField()

    is_published = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{title}'.format(title=self.title)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
        ordering = ('-created_at',)


class Like(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='likes')
    post = models.ForeignKey(Post, related_name='likes')

    def __str__(self):
        return 'Лайк от "{author}" к посту "{post}"'.format(author=self.author, post=self.post)

    class Meta:
        verbose_name = 'Лайк'
        verbose_name_plural = 'Лайки'
        ordering = ('-created_at',)
