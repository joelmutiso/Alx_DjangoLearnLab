from rest_framework import generics, permissions
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    """
    API view to get a list of the current user's notifications.
    """
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Returns notifications for the authenticated user, ordered by timestamp,
        and marks them as read.
        """
        queryset = Notification.objects.filter(recipient=self.request.user).order_by('-timestamp')
        # Mark all notifications as read upon fetching
        queryset.update(is_read=True)
        return queryset