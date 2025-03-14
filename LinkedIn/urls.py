from django.urls import path
from .views import home

urlpatterns = [
    path('home/', home, name='home'),
#    path('delete/<int:post_id>/', delete_post, name='delete_post'),
]
