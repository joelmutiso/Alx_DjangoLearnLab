from django import forms
from django.contrib.auth.models import User

class UserUpdateForm(forms.ModelForm):
    """
    A form to allow authenticated users to update their username and email.
    """
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']
