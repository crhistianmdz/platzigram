from django.db import models

# Create your models here.
class User(models.Model):

    email= models.EmailField(max_length=120, unique=True)
    password=models.CharField(max_length=120)
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    bio=models.TextField(max_length=255)
    birthday=models.DateField(blank=True,null=True)
    created = models.DateField(auto_now_add=True)
    modified=models.DateField(auto_now=True)