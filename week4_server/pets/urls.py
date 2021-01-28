from django.urls import path
from . import views

app_name = "pets"

urlpatterns = [
    path("get/", views.get_pets, name="get-pets"),
    path("create/", views.create, name="pet-create")
]