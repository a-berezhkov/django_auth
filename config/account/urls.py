from django.urls import path
from .views import user_register, index, user_login, user_logout

urlpatterns = [
    path("", index, name="account_index"),
    path("register", user_register, name="account_register"),
    path("login", user_login, name="account_login"),
    path("logout", user_logout, name="account_logout"),
]
