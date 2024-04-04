from django.urls import path
from .views import (login, 
                    register, 
                    logout, 
                    resetPassword,
                    check_user,
                    )

urlpatterns = [
    
    path("login/", login, name="login"),
    path("register/", register, name="register"),
    path("logout/", logout, name="logout"),
    path("reset-password/", resetPassword, name="resetPassword"),
    path("check_user/", check_user, name="check_user"),
]
