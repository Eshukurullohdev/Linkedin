from django.shortcuts import render



def nav(request):
    return render(request, 'nav.html')

def home(request):
    return render(request, 'home.html')

