from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text']
        
        
from Authentication.models import Profil  # Profile modelingiz shu faylda bo‘lishi kerak

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['fullname', 'location', 'profilBanner', 'img', 'bio']

       
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full border border-gray-300 rounded-md shadow-sm focus:ring-blue-500 focus:border-blue-500'
            })
