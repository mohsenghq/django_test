from django.shortcuts import render, get_object_or_404
from .models import Product
from django.views.generic import ListView, DetailView

# Create your views here.

def product_view(request):
    products = Product.objects.all()
    context={
        'products': products
    }
    return render(request, "products/product_view.html", context)


class ProductListView(ListView):
    template_name = "products/product_view.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductListView, self).get_context_data(*args, **kwargs)
        return context
    

def product_detail(request, id=None, *args, **kwargs):
    # instance = Product.objects.get(pk=pk)
    instance = get_object_or_404(Product, id=id)
    context = {
        'product': instance
    }
    return render(request, "products/product.html", context)


class ProductDetailView(DetailView):
    template_name = "products/product.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context