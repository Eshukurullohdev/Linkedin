from django.shortcuts import render
from .models import Profil
# Create your views here.
def profil(request):
    profil = Profil.objects.all()
    return render(request, 'profile.html', {'profil': profil})
