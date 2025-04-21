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
        fields = ['img', 'fullname', 'location', 'bio', 'profilBanner', 'ish']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['img'].widget.attrs.update({
            'class': 'block w-full  text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 focus:outline-none file:cursor-pointer',
        });

        self.fields['fullname'].widget.attrs.update({
            'class': 'mt-2 p-2 outline-none block w-full rounded-xl border-gray-300 shadow-sm focus:border-blue-500 focus:ring focus:ring-blue-200 focus:ring-opacity-50',
            'placeholder': 'To‘liq ismingiz'
        });

        self.fields['location'].widget.attrs.update({
            'class': 'mt-2 p-2 outline-none block w-full rounded-xl border-gray-300 shadow-sm focus:border-green-500 focus:ring focus:ring-green-200 focus:ring-opacity-50',
            'placeholder': 'Yashash joyingiz'
        });

        self.fields['bio'].widget.attrs.update({
            'class': 'mt-2 p-2 outline-none block w-full rounded-xl border-gray-300 shadow-sm focus:border-purple-500 focus:ring focus:ring-purple-200 focus:ring-opacity-50',
            'placeholder': 'Qisqacha bio',
            'rows': 3
        });

        self.fields['profilBanner'].widget.attrs.update({
            'class': 'block p-2 w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-pink-50 file:text-pink-700 hover:file:bg-pink-100',
        });

        self.fields['ish'].widget.attrs.update({
            'class': 'mt-2 p-2 block outline-none w-full rounded-xl border-gray-300 shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50',
            'placeholder': 'Ish joyingiz yoki kasbingiz'
        });
        
    
        

class ProfileImageForm(forms.ModelForm):
    class Meta:
        model = Profil
        fields = ['img']
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['img'].widget.attrs.update({
            'class': 'block w-full  text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100 focus:outline-none file:cursor-pointer',
        })