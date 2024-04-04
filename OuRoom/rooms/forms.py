from django import forms
from django.forms import ModelForm

from .models import Comment, CommentReply

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
