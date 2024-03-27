from django.urls import path
from .views import login, register, logout, validate_registration

urlpatterns = [
    
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("validate_registration/", validate_registration, name="validate_registration"),
    
]
