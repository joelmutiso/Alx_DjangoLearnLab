from django import forms
from django.contrib.auth.models import User
from .models import Post

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
        fields = ['title', 'content']
