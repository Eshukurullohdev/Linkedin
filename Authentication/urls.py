from  django.urls import path
from  .views import *

urlpatterns = [
    path('profile/', profil, name='profile'),
    path('profile/edit/<int:pk>/',  edit_profile, name='edit_profile'),
    path('edit-profile/photo/', update_photo, name='update_photo'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


