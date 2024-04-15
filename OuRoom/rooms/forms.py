from django import forms
from django.forms import ModelForm
from .models import Comment, CommentReply, GroupMembers
from django.contrib.auth import get_user_model
class AddCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ['content']

        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Dodaj komentarz ...'})
        }

        labels = {
            'content': ''
        }

class AddCommentReplyForm(ModelForm):

    class Meta:
        model = CommentReply
        fields = ['content']

        widgets = {
            'content': forms.TextInput(attrs={'placeholder': 'Odpowiedź ...'})
        }

        labels = {
            'content': ''
        }


class AddGroupMemberForm(ModelForm):

    class Meta:
        model = GroupMembers
        fields = ['user', 'role']

    def __init__(self, *args, **kwargs):
        group_id = kwargs.pop('group_id', None)
        super().__init__(*args, **kwargs)
        if group_id:
            User = get_user_model()
            self.fields['user'].queryset = User.objects.exclude(groupmembership__group_id=group_id) #Preventing the same user from being added


