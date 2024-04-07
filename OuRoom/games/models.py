from django.db import models
from django.conf import settings

class Score(models.Model):

    player = models.ForeignKey(settings.AUTH_USER_MODEL)
    point = models.IntegerField()

    def __str__(self):
        return f'{self.player.username} - {self.point}'