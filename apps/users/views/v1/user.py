from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from django.contrib.auth.models import User

from apps.users.serializers.v1.user import UserSerializer


class AdminUserViewSet(ModelViewSet):
    """User CRUD"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
