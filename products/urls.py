from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import (product_view, product_detail, 
                    ProductListView, 
                    ProductDetailView, 
                    ProductActiveView, 
                    ProductActiveDetail,
                    ProductShowWithSlug)

app_name = 'products'

urlpatterns = [
    path('products-fb/', product_view),
    path('products-cb/', ProductListView.as_view()),
    path('products-fb/<id>/', product_detail),
    path('products-cb/<pk>/', ProductDetailView.as_view()),
    path('products-active/', ProductActiveView.as_view()),
    path('products-active/<pk>/', ProductActiveDetail.as_view()),
    path('products/<slug>/', ProductShowWithSlug.as_view()),
]