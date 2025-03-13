from django.shortcuts import render, redirect
from LinkedIn.forms import PostForm
from .models import Post


def nav(request):
    return render(request, 'nav.html')

def home(request):
    
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    else:
        form = PostForm()
        
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html', {'form':form, 'posts': posts })

