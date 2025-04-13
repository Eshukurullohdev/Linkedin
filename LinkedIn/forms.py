from django import forms
from .models import Post
from Authentication.models import Profil

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['image', 'text']
        
        

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = [ 'fullname', 'img', 'location', 'bio', 'profilBanner']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'mt-1 block w-full border border-gray-rounded-md shadow-sm focus:ring-blue-focus:border-blue-500'
            })