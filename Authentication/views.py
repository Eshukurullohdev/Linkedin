from django.shortcuts import render, redirect
from .models import Profil
from LinkedIn.models import Post


def profil(request):
    profil = Profil.objects.all()
    post = Post.objects.all()
    return render(request, 'profile.html', {'profil': profil, 'post': post})




