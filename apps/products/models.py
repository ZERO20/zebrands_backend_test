from django.db import models
from django.contrib.auth.models import User

from .constants import FIELDS_TO_REPORT
from .email import SesEmail

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

    def save(self, *args, **kw):
        updated = False
        data = {}
        if self.pk is not None:
            cls = self.__class__
            old = cls.objects.get(pk=self.pk)
            new = self
            for field in cls._meta.get_fields():
                field_name = field.name
                if field_name in FIELDS_TO_REPORT \
                    and getattr(old, field_name) != getattr(new, field_name):
                    data[field_name] = getattr(new, field_name)
                    updated = True
        super(Product, self).save(*args, **kw)
        if updated:
            self.send_update_notification(changes=data)

    def tracking_detail(self):
        """Create a ProductTrack for the instance"""
        TrackProduct.objects.create(product_id=self.id)

    def send_update_notification(self, changes):
        """Send a update notification when a product is updated
        Args:
            changes dict: fields updated {'field': new_value}
        """
        admin_emails = list(User.objects.filter(is_superuser=True).values_list('email', flat=True))
        subject = 'Product updated!'
        html_content = f"""
            <html>
                <head></head>
                <body>
                <h1 style='text-align:center'>Product updated!</h1>
                <h3>{self.name}</h3>
                <strong>Changes:</strong>
                <br>
                {changes}
                </body>
            </html>
        """
        email = SesEmail(to=admin_emails, subject=subject, html_content=html_content)
        email.send()

class TrackProduct(Common):
    product = models.ForeignKey(Product, related_name="tracks", on_delete=models.CASCADE)

    class Meta:
        indexes = [models.Index(fields=['created_at', ]), ]

    def __str__(self):
        return self.product.name