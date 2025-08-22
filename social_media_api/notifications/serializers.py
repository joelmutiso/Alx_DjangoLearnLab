from rest_framework import serializers
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    """
    Serializer for the Notification model.
    Formats notification data for API responses.
    """
    actor_username = serializers.ReadOnlyField(source='actor.username')
    target_type = serializers.SerializerMethodField()
    
    class Meta:
        model = Notification
        fields = ['id', 'actor_username', 'verb', 'timestamp', 'is_read', 'target_type', 'object_id']

    def get_target_type(self, obj):
        """
        Returns the model name of the target object (e.g., 'post', 'comment').
        """
        if obj.content_type:
            return obj.content_type.model
        return None
