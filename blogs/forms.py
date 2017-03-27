from django import forms


class SortForm(forms.Form):
    sort = forms.ChoiceField(choices=(
        ('title', 'Заголовок'),
        ('description', 'Описание')
    ), initial='title', label='Сортировать по')