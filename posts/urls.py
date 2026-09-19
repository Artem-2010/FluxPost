from django.urls import path
from posts.views import post_create_view
from . import views

app_name = 'posts'

urlpatterns = [
    # 1. Главная страница по адресу '' (теперь вызывает index_view)
    path('', views.index_view, name='index'),

    # 2. Страница ленты по адресу 'feed/'
    path('feed/', views.post_list_view, name='list'),

    # Остальные ваши пути
    path('create/', post_create_view, name='create'),
    path("<slug:post_slug>/", views.post_detail_view, name="detail"),
    path("<slug:post_slug>/update/", views.post_update_view, name="update"),
    path("<slug:post_slug>/delete/", views.post_delete_view, name="delete"),
]