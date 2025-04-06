from django.shortcuts import render
from .models import Profil
from LinkedIn.models import Post
# Create your views here.
def profil(request):
    profil = Profil.objects.all()
    post = Post.objects.all()
    return render(request, 'profile.html', {'profil': profil, 'post': post})
