from django.contrib.auth.models import User, AbstractUser
from django.contrib.auth.models import Group
from django.db import models

from laboratory.models import Laboratory

# Create your models here.

class SystemUser(AbstractUser):
    phone_number = models.CharField(max_length=15, blank=True)
    company = models.CharField(max_length=50, blank=True)
    
    def assign_group(self, group_name):
        group, created = Group.objects.get_or_create(name=group_name)
        self.groups.add(group)
    
    def __str__(self):
        return self.username


class Client(SystemUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.assign_group('Client')


class Manager(SystemUser):
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.assign_group('Manager')


class Technician(SystemUser):
    laboratory = models.ForeignKey(Laboratory, related_name='technicians', on_delete=models.SET_NULL, null=True)
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.assign_group('Technician')
