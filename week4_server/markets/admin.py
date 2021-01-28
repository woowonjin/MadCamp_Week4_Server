from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Market)
class MarketAdmin(admin.ModelAdmin):
    list_display = ("user",
                    "number",
                    "price",
                    "price_per_one")