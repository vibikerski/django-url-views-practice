from django.urls import path
from Products import views

urlpatterns = [
    path("", views.get_all_products, name="products"),
    path("product/<int:product_id>", views.get_product, name="product")
]