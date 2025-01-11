from django.contrib import admin

# Register your models here.

from . import models

admin.site.register(models.SystemUser)
admin.site.register(models.Client)
admin.site.register(models.Manager)
admin.site.register(models.Technician)
