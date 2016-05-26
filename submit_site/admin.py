from django.contrib import admin
from submit_site import models
# Register your models here.

class PropertiesAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.Properties, PropertiesAdmin)
