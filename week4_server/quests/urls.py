from django.urls import path
from . import views

app_name = "quests"

urlpatterns = [
    path("get/", views.get_quest, name="get-quests"),
    path("clear/", views.clear_quest, name="clear-quests"),
]