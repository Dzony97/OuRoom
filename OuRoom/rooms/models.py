from django.db import models
from django.conf import settings
from django.urls import reverse
from django.utils import timezone

class Group(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='creator_group', on_delete=models.CASCADE)
    name = models.TextField(max_length=50)
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('group_detail', kwargs={'group_id': self.id})

class Post(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    time_release = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_like', blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, related_name='group_post' )

    class Meta:
        ordering = ['-time_release']

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk}) #Generate full url

    def total_likes(self):
        return self.like.count()

class GroupMembers(models.Model):

    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='membership')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='group_membership')
    role = models.TextField(max_length=30, default='Członek grupy')
    time_release = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} należy do {self.group.name}'

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







