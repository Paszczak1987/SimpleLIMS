from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class SiteOfficeAddress(models.Model):
    street = models.CharField(max_length=150)
    number = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.street} {self.number}, {self.postal_code} {self.city}, {self.country}"

class BuildingSite(models.Model):
    name = models.TextField()
    short_name = models.CharField(max_length=100, unique=True)
    office_address = models.ForeignKey(SiteOfficeAddress, on_delete=models.SET_NULL, null=True)
    ordering_persons = models.ManyToManyField(User, related_name="building_sites", blank=True)
    
    def __str__(self):
        return f"{self.short_name} ({self.office_address})"
    