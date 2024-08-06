from django.db import models

# Create your models here.


class Game(models.Model):
    type = models.CharField(max_length=100)
    teamone = models.CharField(max_length=100)
    teamtwo = models.CharField(max_length=100)
    gametime = models.DateTimeField()

    def __str__(self):
        return f"{self.type} ({self.teamone} vs. {self.teamtwo})"
