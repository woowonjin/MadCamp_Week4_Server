from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Pet)
class PetAdmin(admin.ModelAdmin):
    list_display = ("user", "kind")