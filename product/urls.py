from django.urls import path
from . import views

urlpatterns = [
    path('list', views.product_list, name="product-list"),
    path('details/<int:id>', views.product_details, name="product-details"),
]