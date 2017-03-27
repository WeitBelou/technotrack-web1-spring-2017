from django import forms

from blogs.models import Post, Blog
from comments.models import Comment


class FilterForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), initial='title', label='Сортировать по', required=True)
    search = forms.CharField(max_length=255, label='Поиск', required=False)


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog', 'title', 'content',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=user)


class CreateCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'text',)

    def __init__(self, *args, **kwargs):
        super(CreateCommentForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(CreateCommentForm, self).is_valid()
