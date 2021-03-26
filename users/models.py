from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE

# Create your models here.
class Profile(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    website= models.URLField(max_length=200,blank=True)
    biography=models.TextField(max_length=500, blank=True)
    phone=models.CharField(max_length=20, blank=True)
    picture=models.ImageField(upload_to='users/picture',blank=True,null=True)
    created=models.DateField(auto_now_add=True)
    modified=models.DateField(auto_now=True)

    def __str__(self):
        return self.user.username
