from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from taggit.models import Tag
from .models import Post
from .forms import PostForm


def post_list_view(request):
    posts = Post.objects.filter(is_published=True).select_related('author')
    
    # Поиск по тегу
    tag_slug = request.GET.get('tag')
    current_tag = None
    
    if tag_slug:
        current_tag = get_object_or_404(Tag, slug=tag_slug)
        posts = posts.filter(tags__in=[current_tag])

    context = {
        'posts': posts,
        'current_tag': current_tag,
    }
    return render(request, 'posts/post_list.html', context)

def post_detail_view(request,post_slug):
    posts = get_object_or_404(Post, slug=post_slug,is_published=True)
    
    context = {
        'posts': posts,
    }

    return render(request, 'posts/post_detail.html', context)

@login_required
def post_create_view(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        print(request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.save()

            return redirect('posts:detail', post_slug=new_post.slug)
    else:
        form = PostForm()

    context = {
        'form': form
    }

    return render(request, 'posts/post_form.html', context)

@login_required
def post_update_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.author != request.user:
        return HttpResponseForbidden("Ошибка 403: У вас нет прав на редактирование чужой записи.")

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:detail', post_slug=post.slug)
    else:
        form = PostForm(instance=post)

    return render(request, 'posts/post_form.html', {'form': form, 'is_edit': True})

@login_required
def post_delete_view(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)

    if post.author != request.user:
        return HttpResponseForbidden("Ошибка 403: Вы не можете удалить чужую статью")

    if request.method == "POST":
        post.delete()
        return redirect('posts:list')

    return render(request, 'posts/post_confirm_delete.html', {'post': post})

def index_view(request):
    return render(request, 'index.html')