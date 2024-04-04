from django.shortcuts import render

# Create your views here.

dashboard_path = "dashboard/"

def dashboard(request):
    return render(request, dashboard_path + "dashboard.html")