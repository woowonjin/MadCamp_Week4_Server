from django.db import models
from core import models as core_models

# Create your models here.
class Market(core_models.TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="markets")
    number = models.IntegerField()
    price = models.IntegerField()

    def price_per_one(self):
        return self.price/self.number