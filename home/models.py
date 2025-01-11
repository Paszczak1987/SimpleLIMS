from django.contrib.auth.models import AbstractUser, Group
from django.db import models

from laboratory.models import Laboratory

# Create your models here.

class SystemUser(AbstractUser):
    phone_number = models.CharField(max_length=20, unique=True, blank=True)
    company = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.username
    
class Client(SystemUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.groups.add(Group.objects.get(name='Client'))
    
    class Meta:
        verbose_name = 'Client'

class Manager(SystemUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.groups.add(Group.objects.get(name='Manager'))
    
    class Meta:
        verbose_name = 'Manager'

class Technician(SystemUser):
    laboratory = models.ForeignKey('laboratory.Laboratory', related_name='technicians', on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.groups.add(Group.objects.get(name='Technician'))
    
    class Meta:
        verbose_name = 'Technician'
    