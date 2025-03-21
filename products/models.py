from django.db import models


class ProductQuerySet(models.query.QuerySet):
    def active(self):
        return self.filter(active=True)

class ProductManager(models.Manager):

    def get_queryset(self):
        return ProductQuerySet(self.model, using=self._db)
    
    def get_product_by_id(self, id):
        qs = self.get_queryset().filter(id=id)
        if qs.count() == 1:
            return qs.first()
        return None
    
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField(default='This is cool!')
    featured = models.BooleanField(default=False)
    image = models.ImageField(upload_to='products/', null=True, blank=True)
    active = models.BooleanField(default=False)

    objects = ProductManager()

    def __str__(self):
        if self.image:
            return f"{self.title} (Image available)"
        return self.title