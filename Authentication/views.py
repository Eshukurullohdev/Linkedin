from django.shortcuts import render, redirect, get_object_or_404
from .models import Profil
from LinkedIn.models import Post
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib import messages
from LinkedIn.forms import ProfileEditForm, ProfileImageForm
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

def edit_profile(request, pk):
    profile = get_object_or_404(Profil, pk=pk)
    if request.method == "POST":
        form = ProfileEditForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileEditForm(instance=profile)
    return render(request, 'edit_profile.html', {'form': form})

def update_photo(request):
    if request.method == 'POST':
        form = ProfileImageForm(request.POST, request.FILES, instance=request.user.profil)
        if form.is_valid():
            form.save()  # Rasmni saqlash
            return redirect('profile')  # Yangilangan rasmni ko'rsatadigan profil sahifasiga yo'naltirish
    else:
        form = ProfileImageForm(instance=request.user.profil)  # Foydalanuvchining profilini formaga uzatish

    return render(request, 'update_photo.html', {'form': form})