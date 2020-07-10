from blog.models import Category, Profile

def my_context(request):
    categories = Category.objects.all()
    profile = Profile.objects.all()
    return {'categories': categories, 'profile': profile}