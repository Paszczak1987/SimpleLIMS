from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Laboratory(models.Model):
    name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=50)
    code = models.CharField(max_length=10)
    
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    manager = models.OneToOneField('home.Manager', related_name='laboratory', on_delete=models.SET_NULL, null=True)