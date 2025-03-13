from  django.urls import path
from Authentication.views import profil

urlpatterns = [
    path('profile/', profil, name='profile'),
]


