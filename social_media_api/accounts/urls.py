from django.urls import path
from .views import UserRegistrationView, UserLoginView, FollowUserView, UnfollowUserView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
    path('follow/<int:user_id>/', FollowUserView.as_view(), name='follow-user'), 
    path('unfollow/<int:user_id>/', UnfollowUserView.as_view(), name='unfollow-user'),
]



