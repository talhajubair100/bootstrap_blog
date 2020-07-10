from blog.models import Category, Profile
from product.models import Category as product_category


def my_context(request):
    categories = Category.objects.all()
    profile = Profile.objects.all()
    p_ctg = product_category.objects.all()

    return {'categories': categories, 'profile': profile, 'p_ctg': p_ctg}