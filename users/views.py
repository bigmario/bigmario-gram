# Models
from users.models import Profile
from django.contrib.auth.models import User

# Libs
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Exceptions

from django.db.utils import IntegrityError

# Create your views here.


def vista(request):
    return HttpResponse("Users")


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("feed")
        else:
            error_context = {"error": "Invalid user and/or password"}
            return render(request, "users/login.html", error_context)

    return render(request, "users/login.html")


@login_required
def logout_view(request):
    logout(request)
    return render(request, "users/login.html")


def signup_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST.get("password", True)
        password_confirmation = request.POST.get("password-confirmation", True)
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]

        if password != password_confirmation:
            error_context = {"error": "Not matching Password Confirmation"}
            return render(request, "users/signup.html", error_context)
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError:
            error_context = {"error": "Duplicated Username"}
            return render(request, "users/signup.html", error_context)

        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.save()

        profile = Profile(user=user)
        profile.save()

        return render(request, "users/login.html")

    return render(request, "users/signup.html")


def update_profile_view(request):
    return render(request, "users/update_profile.html")
