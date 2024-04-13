from django.contrib import admin
from .models import Post, Comment, CommentReply, Group


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Group)