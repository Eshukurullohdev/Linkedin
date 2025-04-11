from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')
    text = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)# Post qachon yaratilganini saqlaydi
    def __str__(self):
        return f"Post {self.id}"
