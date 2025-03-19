from django.shortcuts import render
from .models import Product
from django.views.generic import ListView

# Create your views here.

def product_detail_view(request):
    products = Product.objects.all()
    context={
        'products': products
    }
    return render(request, "products/product_detail.html", context)


class ProductListView(ListView):
    template_name = "products/product_detail.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context