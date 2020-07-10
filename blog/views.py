from django.shortcuts import render
from . models import Post, Category, Profile
# Create your views here.

def search_post(request):
    if request.method == 'POST':
        search_keyword = request.POST['search_keyword']
        posts = Post.objects.filter(title__contains = search_keyword)
        context = {'posts': posts, 'search_keyword': search_keyword}
        return render(request, 'blog/search.html', context)
    return render(request, 'blog/search.html')

def detail_post(request, id):
    post_obj = Post.objects.get(id=id)
    context = {'post': post_obj}
    return render(request, 'blog/post_detail.html', context)

def category_post(request, ctg_name):
    ctg_obj = Category.objects.get(name=ctg_name)
    post_list = Post.objects.filter(category=ctg_obj)
    context = {'posts': post_list, 'ctg_name': ctg_name}
    return render(request, 'blog/post_by_ctg.html', context)