from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Quest)
class QuestAdmin(admin.ModelAdmin):
    list_display = ("user",
                    "npc",
                    "__str__",)