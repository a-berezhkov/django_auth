from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User

# Create your views here.


def user_register(request):
    # регистрация == создание нового User
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("account_index")
    form = UserRegistrationForm()
    return render(request, "account/registration.html", {"form": form})


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(request.POST)
        if form.is_valid():
            # получить логин и пароль
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            # аутентификацию пользователя
            user = authenticate(
                request, username=username, password=password
            )  # User or None
            # SELECT * FORM Users WHERE username = "username" AND password = "password"
            if user is not None:
                # авторизация пользователя
                login(request, user=user)
                return redirect("account_index")
    form = UserLoginForm()
    return render(request, "account/auth.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("account_index")


def index(request):
    users = User.objects.all()
    return render(request, "account/index.html", context={"users": users})
