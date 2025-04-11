from django.shortcuts import render, redirect
from .models import Profil
from LinkedIn.models import Post
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages

def profil(request):
    profil = Profil.objects.all()
    post = Post.objects.all()
    return render(request, 'profile.html', {'profil': profil, 'post': post})



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


def logout(request):
    auth_logout(request)
    return render(request, 'logout.html')


