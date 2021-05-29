from django.shortcuts import render, redirect
from django.contrib.auth.models import auth, User
from django.contrib import messages

# Create your views here.


def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        msg = 0
        if password1 != password2:
            messages.info(request, "Password doesn't match")
            msg += 1
        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken!")
            msg += 1
        if User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            msg += 1
        if msg:
            return redirect('register')
        else:
            user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password1)
            auth.login(request, user)
            return redirect('/')
    else:
        return render(request, "accounts/register.html")


def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "Invalid credentials!")
            return redirect('/accounts/login')
    else:
        return render(request, "accounts/login.html")


def logout(request):
    auth.logout(request)
    print("User logged out")
    return redirect('/')
