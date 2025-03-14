from django.db import models

class PostImg(models.Model):
    img = models.ImageField(upload_to='media/', null=True, blank=True)  # ✅ Rasmlar "media/posts/" ichiga tushadi
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Post {self.id} - {self.date.strftime('%Y-%m-%d %H:%M')}"
