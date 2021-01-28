from django.db import models
from core import models as core_models

# Create your models here.
class Quest(core_models.TimeStampModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="quests")
    problem = models.ForeignKey("problems.Problem", on_delete=models.CASCADE, related_name="quests")
    is_solved = models.BooleanField(default=False)

    HOBIN = "HOBIN"
    HAECHEOL = "HAECHEOL"
    YOONHO = "YOONHO"
    CHANI = "CHANI"
    GANGWOOK = "GANGWOOK"

    NPC_CHOICES = ((HOBIN, HOBIN), (HAECHEOL, HAECHEOL), (YOONHO, YOONHO), (CHANI, CHANI), (GANGWOOK, GANGWOOK))
    
    npc = models.CharField(choices=NPC_CHOICES, max_length=20, default=HOBIN)

    def __str__(self):
        return f"question : {self.problem.question}, answer : {self.problem.answer}, reward : {self.problem.reward}"

    def serialize_custom(self):
        data = {
            "question" : self.problem.question,
            "answer" : self.problem.answer,
            "reward" : self.problem.reward,
            "npc" : self.npc,
        }
    