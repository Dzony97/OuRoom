from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model

from .models import Comment, CommentReply, GroupMembers

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

user = get_user_model()

class AddGroupMember(ModelForm):

    user = forms.ModelChoiceField(queryset=user.objects.all(), label='Użytkownik')

    class Meta:
        model = GroupMembers
        fields = ['user']

