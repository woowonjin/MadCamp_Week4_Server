from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    strawberry = models.IntegerField(default=0)
    point = models.IntegerField(default=0)
    pwd = models.CharField(max_length=100)