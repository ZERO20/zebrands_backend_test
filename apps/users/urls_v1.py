from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from django.urls import path

from apps.users.views.v1.user import AdminUserViewSet

router = routers.DefaultRouter()
router.register(r'users', AdminUserViewSet, basename="users")

urlpatterns = [
    path('token/request/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] + router.urls
