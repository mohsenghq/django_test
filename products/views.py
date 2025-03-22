from django.http import Http404
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
    

def product_detail(request, id=None, *args, **kwargs):
    # product = Product.objects.get(pk=pk)
    # product = get_object_or_404(Product, id=id)
    product = Product.objects.get_product_by_id(id)
    if product is None:
        raise Http404("Product does not exist (function based view)")
    
    # qs = Product.objects.filter(id=id)
    # if qs.exists() and qs.count() == 1:
    #     product = qs.first()
    # else:
    #     raise Http404("Product does not exist (function based view)")
    context = {
        'product': product
    }
    return render(request, "products/product.html", context)


class ProductListView(ListView):
    template_name = "products/product_view.html"
    queryset = Product.objects.all()
    context_object_name = 'products'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     return context
    

class ProductDetailView(DetailView):
    template_name = "products/product.html"
    queryset = Product.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(ProductDetailView, self).get_context_data(*args, **kwargs)
        return context
    
    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_product_by_id(pk)
        if instance is None:
            raise Http404("Product does not exist (class based view)")
        return instance
    

class ProductActiveView(ListView):
    template_name = "products/product_view.html"
    context_object_name = 'products'
    
    def get_queryset(self):
        return Product.objects.all().active()
    

class ProductActiveDetail(DetailView):
    template_name = "products/product.html"

    def get_queryset(self):
        return Product.objects.all().active()

class ProductShowWithSlug(DetailView):
    template_name = "products/product.html"

    def get_object(self, *args, **kwargs):
        slug = self.kwargs.get('slug')
        instance = get_object_or_404(Product, slug=slug)
        return instance


