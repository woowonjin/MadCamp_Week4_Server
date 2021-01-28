from django.db import models
from core import models as core_models

# Create your models here.
class Pet(core_models.TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    
    BIRD = "BIRD"
    CAT = "CAT"
    CHICKEN = "CHICKEN"
    COW = "COW"
    DOG = "DOG"
    DUCK = "DUCK"
    ELEPHANT = "ELEPHANT"
    KOALA = "KOALA"
    LLAMA = "LLAMA"
    PENGUIN = "PENGUIN"

    PET_CHOICES = ((BIRD, BIRD), (CAT, CAT), (CHICKEN, CHICKEN), (COW, COW), (DOG, DOG), (DUCK, DUCK), (ELEPHANT, ELEPHANT), (KOALA, KOALA), (LLAMA, LLAMA), (PENGUIN, PENGUIN))

    kind = models.CharField(choices=PET_CHOICES, max_length=20, default=DOG)

    def serialize_custom(self):
        data = {
            "kind": self.kind,
        }
        return data