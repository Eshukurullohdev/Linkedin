from django.db import models

class Post(models.Model):
    image = models.ImageField(upload_to='posts/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"Post {self.id} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"
