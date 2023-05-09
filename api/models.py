from django.db import models

# Create your models here.
class Products(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductCategory = models.CharField(max_length=100)
    ProductPrice = models.IntegerField()
    ProductImages = models.ImageField()

