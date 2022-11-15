from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet


from apps.products.models import Brand
from apps.products.serializers.v1.brand import BrandSerializer

class BrandViewSet(ModelViewSet):
    """Brand CRUD ModelViewSet"""
    serializer_class = BrandSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        queryset = Brand.objects.filter(active=True)
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('name', openapi.IN_QUERY, description="name", type=openapi.TYPE_STRING)
    ])
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
