from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>', views.detail_post, name="detail-post"),
    path('category/<ctg_name>', views.category_post, name="category-post"),

]