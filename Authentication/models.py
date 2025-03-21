from django.db import models


class Profil(models.Model):
    img = models.ImageField(upload_to='static/img/')
    location = models.CharField(max_length=50)
    bio = models.TextField()
    profilBanner = models.ImageField(upload_to='static/img/')
    fullname = models.CharField(max_length=50)
    
    
    def __str__(self):
        return f"{self.fullname}"
    
    