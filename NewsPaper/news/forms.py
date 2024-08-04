from django import forms
from .models import Post  # Импортируем модель Post


class NewsForm(forms.Form):
    title = forms.CharField(label="Заголовок", max_length=200)
    content = forms.CharField(label="Контент", widget=forms.Textarea)
    # ... другие поля для формы новости


class ArticleForm(forms.Form):
    title = forms.CharField(label="Заголовок", max_length=200)
    content = forms.CharField(label="Контент", widget=forms.Textarea)
