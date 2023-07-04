from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Product(models.Model):
    fname=models.CharField(max_length=30)
    lname=models.CharField(max_length=30)
    uname=models.CharField(max_length=30)
    uemail=models.EmailField(max_length=30)
    upasswd=models.CharField(max_length=30)
    
   
    

