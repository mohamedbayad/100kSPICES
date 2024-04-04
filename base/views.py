from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout as logout_view , login as login_view
from django.contrib.auth.models import User

# Create your views here.

template_path = "authentication/"
dashboard_path = "dashboard/"

def check_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        checkUser = User.objects.filter(username=username).exists()
        if checkUser:
            return JsonResponse({"exists": True, "message": "User already exists"})
    return JsonResponse({"exists": False})

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return JsonResponse({"status": True, "message": "Login successful"})
        else:
            checkUser = User.objects.filter(username=username).exists()
            if checkUser:
                return JsonResponse({"status": False, "message": "Your password is incorrect"})
            return JsonResponse({"status": False, "message": f"The username \"{username}\" is incorrect"})
    return render(request, f"{template_path}login.html", {'title' : "login"})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        if password_confirmation == password:
            user = User.objects.create_user(username, email, password)
            user.save()
        
    return render(request, f'{template_path}register.html')

def logout(request):
    logout_view(request)
    return redirect("login")


def resetPassword(request):
    
    return render(request, f'{template_path}resetPassword.html')
