from pyexpat import model
from django.db import models

# Create your models here.
class Product(models.Model):
    product_Id=models.PositiveIntegerField()
    name=models.CharField(max_length=20)
    