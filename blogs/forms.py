from django import forms

from blogs.models import Post, Blog


class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), initial='title', label='Сортировать по')


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('blog', 'title', 'content',)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(CreatePostForm, self).__init__(*args, **kwargs)
        self.fields['blog'].queryset = Blog.objects.filter(owner=user)
