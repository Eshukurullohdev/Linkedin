from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='posts/')  # Rasm 'media/posts/' ichiga yuklanadi
    created_at = models.DateTimeField(auto_now_add=True)  # Post qachon yaratilganini saqlaydi

    def __str__(self):
        return f"Post {self.id}"
