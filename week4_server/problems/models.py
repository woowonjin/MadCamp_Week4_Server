from django.db import models
from core import models as core_models

# Create your models here.
class Problem(core_models.TimeStampModel):
    question = models.TextField()
    answer = models.CharField(max_length=100)
    reward = models.IntegerField()

    def __str__(self):
        return self.question