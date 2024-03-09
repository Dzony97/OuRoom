from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    comment = models.TextField(max_length=200)
    time_release = models.DateTimeField(default=timezone.now)

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_release = models.DateTimeField(default=timezone.now)
    content = models.TextField()

    image = models.ImageField(null=True, blank=True, upload_to='images/', height_field=None, width_field=None)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk}) #Generate full url




