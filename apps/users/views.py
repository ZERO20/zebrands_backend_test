
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet

from django.contrib.auth.models import User

from .serializers import UserSerializer


class AdminUserViewSet(ModelViewSet):
    """User CRUD"""
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated,]
    queryset = User.objects.all()
