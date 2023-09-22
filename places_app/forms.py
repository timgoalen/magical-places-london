from django import forms
from .models import Comment


# class PlaceCreateForm(forms.ModelForm)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("comment",)
