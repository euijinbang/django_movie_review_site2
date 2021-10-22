from django import forms
from .models import Comment, Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        exclude = ('user', 'like_users', )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )