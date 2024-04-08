from django.urls import path
from django.contrib.auth import views as auth_view
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
    path("check_user/", check_user, name="check_user"),
    
    path("reset-password/", auth_view.PasswordResetView.as_view(template_name='authentication/reset_password/resetPassword.html'), name="reset_password"),
    path("reset-password-sent/", auth_view.PasswordResetDoneView.as_view(template_name="authentication/reset_password/passwordResetSent.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/", auth_view.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset-password-complete/", auth_view.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
