import uuid
from django.db import models
from django.conf import settings
from django.utils.text import slugify
from unidecode import unidecode
from taggit.managers import TaggableManager


# --- АБСТРАКТНАЯ БАЗОВАЯ МОДЕЛЬ ---
class TimeStampedModel(models.Model):
    """
    АБСТРАКТНЫЙ БАЗОВЫЙ КЛАСС.
    Обеспечивает дочерние классы полями даты создания и изменения.
    """
    created_at = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        abstract = True


# --- БАЗОВАЯ МОДЕЛЬ ПУБЛИКАЦИИ ---
class Post(TimeStampedModel):
    """
    Модель публикации (Статьи)
    Наследует created_at и updated_at от TimeStampedModel
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    cover_image = models.ImageField(
        upload_to='posts/covers/%Y/%m/',
        blank=True,
        null=True,
        verbose_name="Обложка"
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='posts', 
        verbose_name='Автор'
    )
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="URL-слаг")
    content = models.TextField(verbose_name="Содержимое публикации")
    is_published = models.BooleanField(default=True, db_index=True, verbose_name="Опубликовано")
    
    # Менеджер тегов
    tags = TaggableManager(blank=True)

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ['-created_at']

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(unidecode(self.title))
        super().save(*args, **kwargs)