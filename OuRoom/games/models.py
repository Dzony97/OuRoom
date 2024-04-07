from django.db import models
from django.conf import settings

class Score(models.Model):

    player = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    point = models.IntegerField()
    player_username = models.CharField(max_length=30) # Stores the username

    def __str__(self):
        return f'{self.player_username} - {self.point}'