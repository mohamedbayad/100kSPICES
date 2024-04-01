from django.urls import path
from .views import login, register, logout, check_user, dashboard

urlpatterns = [
    
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("check_user/", check_user, name="check_user"),
    path("dashboard/", dashboard, name="dashboard"),
]
