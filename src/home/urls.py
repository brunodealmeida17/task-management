from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('home/', views.home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='perfil_users/login.html'), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),
]
