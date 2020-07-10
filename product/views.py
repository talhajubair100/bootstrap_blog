from django.shortcuts import render
from .models import *

# Create your views here.
def product_list(request):
    products = Product.objects.order_by('-id')
    context = {'products': products}
    return render(request, 'product/product_list.html', context)

def product_details(request, id):
    p_obj = Product.objects.get(id=id)
    context = {'pro_obj': p_obj}
    return render(request, 'product/product_details.html', context)