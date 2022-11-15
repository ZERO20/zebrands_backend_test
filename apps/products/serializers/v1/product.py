from rest_framework import serializers

from apps.products.models import Brand, Product
from apps.products.serializers.v1.brand import BrandSerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(read_only=True)
    brand_id = serializers.PrimaryKeyRelatedField(
        write_only=True,
        queryset=Brand.objects.filter(active=True),
        source="brand"
    )
    class Meta:
        model = Product
        fields = ['id', 'name', 'brand', 'brand_id', 'sku', 'price', 'created_at',]
