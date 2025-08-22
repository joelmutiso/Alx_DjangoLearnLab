from rest_framework import serializers
from .models import Post, Comment, Like
from accounts.serializers import UserRegistrationSerializer

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    Includes a nested author field to display the username.
    """
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ['id', 'author', 'post', 'content', 'created_at', 'updated_at']

class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for the Post model.
    Includes nested author and comments, plus a like count.
    """
    author = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    like_count = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'author', 'title', 'content', 'created_at', 'updated_at', 'comments', 'like_count']
        read_only_fields = ['author']

    def get_like_count(self, obj):
        """
        Custom method to get the number of likes for a post.
        """
        return obj.likes.count()

class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model.
    """
    class Meta:
        model = Like
        fields = ['id', 'user', 'post', 'created_at']
        read_only_fields = ['user', 'post', 'created_at']