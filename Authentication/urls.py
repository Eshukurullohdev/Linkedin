from  django.urls import path
from  .views import *

urlpatterns = [
    path('profile/', profil, name='profile'),
    path('profile/edit/<int:pk>/',  edit_profile, name='edit_profile'),
   path('edit-profile/photo/', update_photo, name='update_photo'),  # Rasmni yangilash URL'si
    path('phote_update/', update_photo, name='phote_update'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
]


