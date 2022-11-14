from django.db import models

class Common(models.Model):
    """Base model for records"""
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    active = models.BooleanField(verbose_name="Active", default=True)

    class Meta:
        abstract = True


class Brand(Common):
    """Model definition for Brand."""
    name = models.CharField(verbose_name="Name", max_length=200)

    class Meta:
        ordering = ["name"]
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'

    def __str__(self):
        return self.name


class Product(Common):
    """Model for products"""
    name = models.CharField(verbose_name="Name", max_length=200)
    sku = models.CharField(verbose_name="SKU", max_length=50, unique=True)
    brand = models.ForeignKey(Brand, verbose_name="Brand", on_delete=models.CASCADE, related_name='products')
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name

    def tracking_detail(self):
        """Create a ProductTrack for the instance"""
        TrackProduct.objects.create(product_id=self.id)

class TrackProduct(Common):
    product = models.ForeignKey(Product, related_name="tracks", on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['created_at', ]), ]

    def __str__(self):
        return self.product.name