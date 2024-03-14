from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, logout as logout_view , login as login_view
from django.contrib.auth.models import User



# Create your views here.

template_path = "authentication/"

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return HttpResponse('login successful')
        else:
            return HttpResponse("login failed")
    return render(request, f"{template_path}login.html", {'title' : "login"})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        user_check = User.objects.filter(username=username).exists()
        if user_check:
            return HttpResponse('the user is already registered')
        else:
            user = User.objects.create_user(username, email, password_confirmation)
            user.save()
            if user is not None:
                return HttpResponse('register successful')
        
    return render(request, f'{template_path}register.html')

def logout(request):
    logout_view(request)
    return HttpResponse('logout successful')