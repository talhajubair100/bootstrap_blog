from django.urls import path
from . import views

urlpatterns = [
    path('list', views.product_list, name="product-list"),
    path('details/<int:id>', views.product_details, name="product-details"),
    path('category/<ctg_name>', views.category_post, name="p-category-post"),
    
]