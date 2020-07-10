from django.shortcuts import render
from blog.models import Post

def home(request):
    posts = Post.objects.order_by('-id')
    context = {'posts': posts}
    return render(request, 'blog/post_list.html', context)