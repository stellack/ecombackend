from django.db import models
from utils.model_abstracts import Model
from django_extensions.db.models import (
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel
)

class Contact(
    TimeStampedModel,
    ActivatorModel,
    TitleDescriptionModel,
    Model
):
    class Meta:
        verbose_name_plural = "Contacts"

    email = models.EmailField(verbose_name="Email")

    def __str__(self):
        return f'{self.title}'




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

    def __str__(self):
         return self.name

class Product(models.Model):
    ProductId = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=200)
    ProductCategory = models.CharField(max_length=100)
    ProductPrice = models.IntegerField()
    ProductImages = models.ImageField()

