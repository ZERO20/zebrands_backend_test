from rest_framework import routers

from django.urls import path

from .views import BrandViewSet, HealthCheckAPIView, ProductViewSet

router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename="products")
router.register(r'brands', BrandViewSet, basename="brands")

urlpatterns = [
    path('', HealthCheckAPIView.as_view(), name='health-check'),
] + router.urls
