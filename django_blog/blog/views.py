from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

def home_view(request):
    """Renders the home page template."""
    return render(request, 'blog/home.html')

def posts_view(request):
    """Renders a placeholder page for blog posts."""
    return render(request, 'blog/posts.html')

def register_view(request):
    """
    Handles user registration.
    
    If the request method is POST, it validates the UserCreationForm,
    saves the new user, logs them in, and redirects to the home page.
    Otherwise, it displays an empty registration form.
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile_view(request):
    """
    Handles the user profile page.
    
    Requires an authenticated user to access. Displays the user's profile details.
    """
    return render(request, 'blog/profile.html')

@login_required
def edit_profile_view(request):
    """
    Handles viewing and editing the user's profile.
    
    If the request is POST, it processes the UserUpdateForm to save changes.
    Otherwise, it displays the form pre-filled with the current user data.
    """
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})
