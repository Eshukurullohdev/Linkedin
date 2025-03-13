from django.db import models

# Create your models here.
class Profil(models.Model):
    username = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/', null=True, blank=True)
    location = models.CharField(max_length=50)
    bio = models.TextField()
    