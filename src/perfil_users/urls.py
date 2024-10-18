from django.urls import path
from django.contrib.auth import views as auth_views
from .views import ProfileListView, ProfileCreateView, ProfileUpdateView, ProfileDeleteView

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='perfil_users/login.html'), name="login"),
    path('logout/', auth_views.logout_then_login, name="logout"),

    path('', ProfileListView.as_view(), name='profile_list'),
    path('create/', ProfileCreateView.as_view(), name='profile_create'),
    path('update/<int:pk>/', ProfileUpdateView.as_view(), name='profile_update'),
    path('delete/<int:pk>/', ProfileDeleteView.as_view(), name='profile_delete'),
]
