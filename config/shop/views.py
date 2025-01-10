from django.shortcuts import render, get_object_or_404, redirect

from .models import Product, Customer, Cart, CartItem, Order, OrderItem


# Create your views here.
def index(request):
    products = Product.objects.all()
    return render(request, "shop/index.html", {"products": products})


def detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, "shop/detail.html", {"product": product})


def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except:
        return redirect("shop_index")
    first_name = request.user.first_name
    last_name = request.user.last_name
    email = request.user.email
    customer, _ = Customer.objects.get_or_create(
        first_name=first_name, last_name=last_name, email=email
    )
    cart, _ = Cart.objects.get_or_create(customer=customer)
    try:
        cart_item = CartItem.objects.get(cart=cart, product=product)
        cart_item.quantity += 1
        cart_item.save()
    except:
        CartItem.objects.create(cart=cart, product=product, quantity=1)
    return redirect("shop_view_cart")


def view_cart(request):
    email = request.user.email
    customer = Customer.objects.get(email=email)
    try:
        cart = Cart.objects.get(customer=customer)
    except:
        return redirect("shop_index")
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, "shop/cart.html", {"cart_items": cart_items})


def make_order(request):
    email = request.user.email
    try:
        customer = Customer.objects.get(email=email)
    except:
        return redirect("shop_index")
    try:
        cart = Cart.objects.get(customer=customer)
    except:
        return redirect("shop_index")
    cart_items = CartItem.objects.filter(cart=cart)
    order = Order.objects.create(customer=customer)
    for cart_item in cart_items:
        OrderItem.objects.create(
            order=order, product=cart_item.product, quantity=cart_item.quantity
        )
    cart.delete()
    return redirect("shop_orders")


def order_list(request):
    customer = Customer.objects.get(email=request.user.email)
    orders = Order.objects.all()
    return render(request, "shop/orders.html", {"orders": orders})
