from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # General blog pages
    path('', views.home_view, name='home'),
    path('posts/', views.posts_view, name='posts'),

    # User authentication paths
    path('register/', views.register_view, name='register'),
    path('profile/', views.profile_view, name='profile'),
    path('profile/edit/', views.edit_profile_view, name='edit_profile'),

    # Explicitly use Django's built-in auth views with our templates
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='blog/logout.html'), name='logout'),

    # This is a fallback and provides other auth URLs, but we override login/logout
    path('', include('django.contrib.auth.urls')),
]
