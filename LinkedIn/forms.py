from django import forms
from .models import PostImg
class PostForm(forms.ModelForm):
    class Meta:
        model = PostImg
        fields = ['img'] # ✅ Faqat rasm yuklash uchun forma
