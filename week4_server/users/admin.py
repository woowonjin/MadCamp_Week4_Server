from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (("CustomProfile", {
        "fields": (
            "strawberry",
            "point",
            "pwd",
        )
    }), )

    list_display = ("username", "strawberry", "point")