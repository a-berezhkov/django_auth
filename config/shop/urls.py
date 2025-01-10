from django.urls import path
from .views import index, detail, add_to_cart, view_cart, order_list, make_order


urlpatterns = [
    path("", index, name="shop_index"),
    path("detail/<int:pk>", detail, name="shop_detail"),
    path("add-to-cart/<int:product_id>", add_to_cart, name="shop_add_to_cart"),
    path("view_cart", view_cart, name="shop_view_cart"),
    path("orders", order_list, name="shop_orders"),
    path("make-order", make_order, name="shop_make_order"),
]
