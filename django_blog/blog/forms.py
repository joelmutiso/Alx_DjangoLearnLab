from django import forms
from django.contrib.auth.models import User
from taggit.forms import TagWidget # Add this import
from .models import Post, Comment

class UserUpdateForm(forms.ModelForm):
    """
    A form to allow authenticated users to update their username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    """
    Form for creating and updating a blog post.
    """
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),
        }

class CommentForm(forms.ModelForm):
    """
    Form for creating and updating a comment.
    """
    class Meta:
        model = Comment
        fields = ['content']
