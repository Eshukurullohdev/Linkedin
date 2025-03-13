from django.shortcuts import render
from .models import Profil  
def profil(request):
    profil = Profil.objects.all()
    return render(request, 'profile.html', {'profil':profil})
