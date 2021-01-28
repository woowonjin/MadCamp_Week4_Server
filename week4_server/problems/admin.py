from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Problem)
class QuestAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "reward")