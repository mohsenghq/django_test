from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__', 'title', 'price', 'active']
    # search_fields = ['title', 'price']
    list_editable = ['price']
    class Meta:
        model = Product

# Register your models here.
admin.site.register(Product, ProductAdmin)