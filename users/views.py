from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, logout, login, get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserUpdateForm, ProfileUpdateForm

User = get_user_model()

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('posts:list')
    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form':form})

def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            login(request,form.get_user())
            return redirect('posts:list')
    else:
        form = AuthenticationForm()
    
    return render(request, 'users/login.html', {'form':form})

def logout_view(request):
    logout(request)
    return redirect('posts:list')

def author_profile_view(request, username):
    author = get_object_or_404(User, username=username)

    author_posts = author.posts.filter(is_published=True).order_by('-created_at')

    context = {
        'author': author,
        'author_post': author_posts
    }

    return render(request,'users/author_profile.html', context)

@login_required
def profile_edit_view(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            messages.success(request, 'Ваш профиль был успешно обновлен!')
            return redirect('users:profile_edit')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'users/profile_edit.html', context)