from django import forms
from .models import CustomUser, Position
from django.contrib.auth.forms import UserCreationForm

class CustomUserForm(UserCreationForm): 

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'groups', 'is_staff', 'is_active', 'is_superuser', 'position', 'phone', 'birth', 'description', 'user_permissions', ]
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'birth': 'Data de Nascimento',
            'phone': 'Telefone',
            'username': 'Usuario',
        }
        

class PositionForms(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position']