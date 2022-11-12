from django.db import models

class Common(models.Model):
    created_at = models.DateTimeField(verbose_name="Created at", auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name="Updated at", auto_now=True)
    active = models.BooleanField(verbose_name="Active", default=True)

    class Meta:
        abstract = True


class Product(Common):
    name = models.CharField(verbose_name="Name", max_length=200)
    sku = models.CharField(verbose_name="SKU", max_length=50)
    brand = models.CharField(verbose_name="Brand", max_length=200)
    price = models.DecimalField(verbose_name="Price", max_digits=10, decimal_places=2)

    class Meta:
        ordering = ["name"]
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
