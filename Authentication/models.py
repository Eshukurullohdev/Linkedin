from django.db import models
from django.contrib.auth.models import User

class Profil(models.Model):
    img = models.ImageField(upload_to='static/img/')
    location = models.CharField(max_length=50)
    bio = models.TextField()
    ish = models.CharField(max_length=200,  null=True)
    profilBanner = models.ImageField(upload_to='static/img/')
    fullname = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"Profile {self.pk}"
    
    