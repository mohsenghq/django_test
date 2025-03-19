from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import product_detail_view, ProductListView

app_name = 'products'

urlpatterns = [
    path('products-fb', product_detail_view),
    path('products-cbv', ProductListView.as_view()),
]