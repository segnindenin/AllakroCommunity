from django.contrib import admin

# Register your models here.
from . import models


admin.site.register(models.Projects)
admin.site.register(models.Markaz)
admin.site.register(models.HealthData)