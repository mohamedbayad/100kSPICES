from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth import authenticate, logout as logout_view , login as login_view
from django.contrib.auth.models import User




# Create your views here.

template_path = "authentication/"

def validate_registration(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        password_confirmation = request.POST.get('password_confirmation')
        
        checkUser = User.objects.filter(username=username).exists()
        
        if checkUser:
            return JsonResponse({"message": "the user is already registered", "from": "username"})
        
        if password != password_confirmation:
            return JsonResponse({"message": "passwords do not match", "from": "password_confirmation"})
    return render(request, f'{template_path}register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_view(request, user)
            return JsonResponse({"status": True, "message": "Login successful"})
        else:
            return JsonResponse({"status": True, "message": "login failed"})
    return render(request, f"{template_path}login.html", {'title' : "login"})

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # password_confirmation = request.POST.get('password_confirmation')
        
        # checkUser = User.objects.filter(username=username).exists()
        
        # if checkUser:
        #     return JsonResponse({"message": "the user is already registered", "from": "username"})
        
        # if password != password_confirmation:
        #     return JsonResponse({"message": "passwords do not match", "from": "password_confirmation"})
        
        user = User.objects.create_user(username, email, password)
        user.save()

        
    return render(request, f'{template_path}register.html')

def logout(request):
    logout_view(request)
    
    return HttpResponse('logout successful')