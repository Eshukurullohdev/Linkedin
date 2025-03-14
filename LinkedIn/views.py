from django.shortcuts import render
# from LinkedIn.forms import PostForm
# from .models import Post
# from Authentication.models import Profil

def nav(request):
    return render(request, 'nav.html')

def home(request):
    # profile = Profil.objects.all()
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         form.save()
    #         return redirect('home')
        
    # else:
    #     form = PostForm()
        
    # posts = Post.objects.all().order_by('-created_at')
    return render(request, 'home.html',)


# def delete_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)  # Post mavjudligini tekshiramiz
#     post.delete()  # Postni bazadan o‘chiramiz
#     return redirect('home')

#  {'form':form, 'posts': posts, 'profile': profile, }