from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.SiteOfficeAddress)
admin.site.register(models.BuildingSite)
