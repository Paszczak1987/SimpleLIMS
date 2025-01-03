from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class UserAdditionalInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='extra_info')
    phone_number = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=50, blank=True)
    
    def __str__(self):
        return self.user.username
