from django.shortcuts import render, redirect, get_object_or_404
from .models import PostImg
from .forms import PostForm

def nav(request):
    return render(request, 'nav.html')

# 📌 1️⃣ Asosiy sahifa – postlarni chiqarish va qo‘shish
def home(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)  # Rasm yuklash uchun request.FILES kerak
        if form.is_valid():
            form.save()
            return redirect('home')  # Post qo‘shilgach, sahifani qayta yuklash
    else:
        form = PostForm()

    posts = PostImg.objects.order_by('-date')  # Eng yangi postlar birinchi chiqishi uchun
    return render(request, 'home.html', {'form': form, 'posts': posts})



# def delete_post(request, post_id):
#     post = get_object_or_404(Post, id=post_id)  # Post mavjudligini tekshiramiz
#     post.delete()  # Postni bazadan o‘chiramiz
#     return redirect('home')

#  {'form':form, 'posts': posts, 'profile': profile, }