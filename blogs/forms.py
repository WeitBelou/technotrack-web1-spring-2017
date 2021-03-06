from django import forms

from blogs.models import Post, Blog
from comments.models import Comment


class FilterForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), label='Сортировать по', required=False)

    search = forms.CharField(max_length=255, label='Поиск', required=False)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog', 'title', 'content', 'is_published')
        labels = {
            'blog': 'Блог',
            'title': 'Заголовок',
            'content': 'Текст поста',
            'is_published': 'Опубликованный',
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=user)


class UpdatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_published')
        labels = {
            'title': 'Заголовок поста',
            'content': 'Текст поста',
            'is_published': 'Опубликованный',
        }

class DeletePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'is_published')
        labels = {
            'title': 'Заголовок поста',
            'content': 'Текст поста',
            'is_published': 'Опубликованный',
        }


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        labels = {
            'text': 'Комментарий'
        }

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CreateCommentForm, self).is_valid()


class CreateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'categories')
        labels = {
            'title': 'Название блога',
            'description': 'Краткое описание блога',
            'categories': 'Набор категорий блога'
        }


class UpdateBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title', 'description', 'categories')
        labels = {
            'title': 'Название блога',
            'description': 'Краткое описание блога',
            'categories': 'Набор категорий блога'
        }


class DeleteBlogForm:
    class Meta:
        model = Blog
        fields = ('title', 'description', 'categories')
        labels = {
            'title': 'Название блога',
            'description': 'Краткое описание блога',
            'categories': 'Набор категорий блога'
        }
