from django.db import models


class Car(models.Model):
    model = models.CharField(max_length=1000, default="Toyota")
    speed = models.IntegerField(default=120)
    color = models.CharField(max_length=16, default="red")

    def __str__(self):
        return f"{self.color} {self.model}, speed: {self.speed}"