from django.urls import path
from .views import register, index

urlpatterns = [
    path("register", register, name="account_register"),
    path("", index, name="account_index"),
    ]
