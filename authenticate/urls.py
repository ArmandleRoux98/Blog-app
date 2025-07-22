from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register_user, sign_user_out

app_name = "authenticate"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="authenticate/login.html"), name="login"),
    path("register/", register_user, name="register"),
    path("logout/", sign_user_out, name="logout"),
]