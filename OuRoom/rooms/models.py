from django.db import models
from django.conf import settings
from django.utils import timezone

class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    time_release = models.DateTimeField(default=timezone.now)

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_release = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField()
    comment = models.ManyToManyField(Comment, blank=True)



