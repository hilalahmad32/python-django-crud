from django.db import models

# Create your models here.
class Product(models.Model):
    title=models.CharField(max_length=255)
    price=models.CharField(max_length=255)
    content=models.CharField(max_length=255)