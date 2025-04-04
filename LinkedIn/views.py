from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from Authentication.models import Profil
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def nav(request):
    return render(request, 'nav.html')


def home(request):
    profile = Profil.objects.all()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Rasm yuklash uchun request.FILES kerak
        if form.is_valid():
            form.save()
            return redirect('home')  # Post qo‘shilgach, sahifani qayta yuklash
    else:
        form = PostForm()

    posts = Post.objects.order_by('-created_at')  # Eng yangi postlar birinchi chiqishi uchun
    return render(request, 'home.html', {'form': form, 'posts': posts, 'profile': profile})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)  # Post mavjudligini tekshiramiz
    post.delete()
    return redirect('home')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, 'Siz tizimga kirdingiz')
            return redirect('home')
        else:
            messages.error(request, 'Login yoki parol xato')
            return redirect('login')
    return render(request, 'login.html') 


