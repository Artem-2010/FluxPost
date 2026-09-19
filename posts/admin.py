from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'is_published', 'created_at', 'updated_at')
    list_filter = ('is_published', 'created_at')
    search_fields = ('title', 'content')

    # Поля, доступные только для чтения в интерфейсе
    readonly_fields = ('id', 'created_at', 'updated_at')

    # Автоматически заполнять поле slug на основе поля title
    prepopulated_fields = {'slug': ('title',)}
