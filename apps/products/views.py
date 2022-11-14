
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet


from .models import Brand, Product
from .serializers import BrandSerializer, ProductSerializer

class HealthCheckAPIView(APIView):
    """Health Check for the API"""

    def get(self, request):
        return Response(data={"status": "Hello world!"}, status=status.HTTP_200_OK)


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


class ProductViewSet(ModelViewSet):
    """Product CRUD ModelViewSet"""
    serializer_class = ProductSerializer
    permission_classes_by_action = {
        'create': [IsAuthenticated],
        'list': [AllowAny],
        'retrieve': [AllowAny]
    }

    def get_queryset(self):
        queryset = Product.objects.filter(active=True)
        name = self.request.query_params.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name)
        return queryset

    def list(self, request):
        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk):
        product = self.get_object()
        serializer = self.get_serializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
