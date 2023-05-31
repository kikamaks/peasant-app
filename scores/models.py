from django.db import models


class Peasant(models.Model):
    name = models.CharField(max_length=256)
    score = models.IntegerField(default=0)
    achievements = models.TextField(blank=True)
    username = models.CharField(max_length=256, blank=True)
    password = models.CharField(max_length=256, blank=True)

    objects = models.Manager

    def __str__(self):
        return self.name



