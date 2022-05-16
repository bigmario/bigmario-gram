from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

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
