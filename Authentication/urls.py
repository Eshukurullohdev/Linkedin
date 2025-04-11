from  django.urls import path
from  .views import *

urlpatterns = [
    path('profile/', profil, name='profile'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


