from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.detail_post, name="detail-post"),
    path('category/<ctg_name>', views.category_post, name="category-post"),
    path('search', views.search_post, name='search'),
    path('create/category', views.create_category, name='create-category'),
    path('create/post', views.create_post, name='create-post'),



]