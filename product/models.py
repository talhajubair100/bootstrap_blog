from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='products')
    description = models.TextField()
    price = models.IntegerField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name