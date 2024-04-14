from django.contrib import admin
from .models import Post, Comment, CommentReply, Group, GroupMembers


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(CommentReply)
admin.site.register(Group)
admin.site.register(GroupMembers)