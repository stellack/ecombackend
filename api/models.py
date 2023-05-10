from django.db import models

# STATE_CHOICE = ((
#     ()
# ))

# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    dob = models.DateField(auto_now=False, auto_now_add=False)
    # state = models.CharField(choices=STATE_CHOICE, max_length=50)
    gender = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    profileimage = models.ImageField(upload_to = 'profileimages', blank=True)
    rdoc = models.FileField(upload_to='rdocs', blank=True)

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductCategory = models.CharField(max_length=100)
    ProductPrice = models.IntegerField()
    ProductImages = models.ImageField()

