from rest_framework import routers

from django.urls import path

from .views import AdminUserViewSet

router = routers.DefaultRouter()
router.register(r'users', AdminUserViewSet, basename="users")

urlpatterns = [
] + router.urls
