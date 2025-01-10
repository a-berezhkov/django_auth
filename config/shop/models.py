from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=250)
    price = models.IntegerField()

    category = models.ForeignKey("Category", on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f" {self.first_name} почта {self.email}"

    def full_name(self):
        return f" {self.first_name} {self.last_name}"


class Order(models.Model):
    created_at = models.DateField(auto_now_add=True)

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Покупатель {self.customer.full_name} купил товар в {self.created_at}"


class OrderItem(models.Model):
    quantity = models.PositiveIntegerField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return f"Товар {self.product.name} из заказа №#{self.order.id} в кол-ве {self.quantity}"


class Cart(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)

    def __str__(self):
        return f"Корзина {self.id} покупателя  {self.customer.full_name} "


class CartItem(models.Model):
    quantity = models.PositiveIntegerField()

    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f"Товар {self.product.name} из корзины №#{self.cart.id} в кол-ве {self.quantity}"
