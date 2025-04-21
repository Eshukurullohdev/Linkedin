from  django.urls import path
from  .views import *

urlpatterns = [
    path('profile/', profil, name='profile'),
    path('profile/edit/<int:pk>/',  edit_profile, name='edit_profile'),  # Rasmni yangilash URL'si
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


