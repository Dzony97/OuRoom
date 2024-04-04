from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone


class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_release = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like', blank=True)

    class Meta:
        ordering = ['-time_release']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk}) #Generate full url

    def total_likes(self):
        return self.like.count()

class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=200)
    time_release = models.DateTimeField(default=timezone.now)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    
    class Meta:
        ordering = ['-time_release']

    def __str__(self):
        return f'{self.author} : {self.content}'

class CommentReply(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comment_reply')
    content = models.TextField(max_length=100)
    time_release = models.DateTimeField(default=timezone.now)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='comment_reply')

    class Meta:
        ordering = ['-time_release']

    def __str__(self):
        return f'{self.author} : {self.content}'







