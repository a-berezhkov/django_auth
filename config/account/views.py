from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, UserLoginForm

from django.contrib.auth.models import User

# Create your views here.


def register(request):
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
            # сделать индентификацию и авторизацию
            return redirect("account_index")
    form = UserLoginForm()
    return render(request, "account/auth.html", {"form": form})


def index(request):
    users = User.objects.all()
    return render(request, "account/index.html", context={"users": users})
