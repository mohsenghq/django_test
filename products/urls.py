from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_view, product_detail, ProductListView

app_name = 'products'

urlpatterns = [
    path('products-fb', product_view),
    path('products-cb', ProductListView.as_view()),
    path('products-fb/<int:pk>/', product_detail),
]