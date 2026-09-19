from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # Добавили 'tags'
        widgets = {
            'tags': forms.TextInput(attrs={
                'placeholder': 'Введите теги через запятую (например: юмор, новости)',
                'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2'
            }),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'cover_image', 'content', 'is_published']
    
    widgets = {
        'cover_image': forms.ClearableFileInput(attrs={
            'class': 'w-full px-4 py-2 text-sm text slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 cursor-pointer',
            'id': 'image-upload-input',
        }),
        'title': forms.TextInput(attrs={
            'class': 'w-full px-4 py-3 rounded=xl border border-slate-300 focus:border-blue-50 focus:ring-2 outline-none transition-all',
            'placeholder': 'Например: Архитектура микросервисов'
        }),
        'content': forms.Textarea(attrs={
            'class': 'w-full px-4 py-3 rounded=xl border border-slate-300 focus:border-blue-50 focus:ring-2 outline-none transition-all',
            'placeholder': 'Напишите текст здесь...'
        }),
        'is_published': forms.CheckboxInput(attrs={
            'class': 'w-5 h-5 text-blue-600 bg-gray-100 border-gray-300 border border-slate-300 focus:ring-blue-500 cursor-pointer'
        })
    }

    labels = {
        'title': 'Заголовок публикации',
        'content': 'текст публикации',
        'is_published': 'Опубликовать сразу?'
    }