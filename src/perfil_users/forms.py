import re  # Importar o módulo re para expressões regulares
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Position

class CustomUserForm(forms.ModelForm):
    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
    )
    confirm_password = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        min_length=8,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'position', 'phone', 'birth', 'description', 'is_staff', 'is_active', 'is_superuser', 'groups', 'password']
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'birth': 'Data de Nascimento',
            'phone': 'Telefone',
            'username': 'Usuário',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")
                
        errors = []
        if len(password) < 8:
            errors.append("A senha deve ter pelo menos 8 caracteres.")
        if not re.search(r'[A-Z]', password):
            errors.append("A senha deve conter pelo menos uma letra maiúscula.")
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            errors.append("A senha deve conter pelo menos um caractere especial.")

        if errors:
            raise forms.ValidationError(errors)   
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])        
        if commit:
            user.save()
            user.groups.set(self.cleaned_data.get('groups', []))            
        return user


class CustomUserUpdateForm(forms.ModelForm):
    password = forms.CharField(
        label='Nova Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,  
        min_length=8,
    )
    confirm_password = forms.CharField(
        label='Confirme a Nova Senha',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        required=False,
        min_length=8,
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'position', 'phone', 'birth', 'description', 'is_staff', 'is_active', 'is_superuser', 'groups']
        widgets = {
            'birth': forms.DateInput(attrs={'type': 'date'}),
        }
        labels = {
            'birth': 'Data de Nascimento',
            'phone': 'Telefone',
            'username': 'Usuário',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        self.fields['groups'].queryset = Group.objects.all()
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("As senhas não coincidem.")        
        errors = []
        if password:  
            if len(password) < 8:
                errors.append("A nova senha deve ter pelo menos 8 caracteres.")
            if not re.search(r'[A-Z]', password):
                errors.append("A nova senha deve conter pelo menos uma letra maiúscula.")
            if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
                errors.append("A nova senha deve conter pelo menos um caractere especial.")

        if errors:
            raise forms.ValidationError(errors)

    def save(self, commit=True):
        user = super().save(commit=False)
        user.password = make_password(self.cleaned_data['password'])        
        if commit:
            user.save()
            user.groups.set(self.cleaned_data.get('groups', []))            
        return user



class PositionForm(forms.ModelForm):
    class Meta:
        model = Position
        fields = ['position']
        widgets = {
            'position': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'position': 'Título da Posição',
        }

    def __init__(self, *args, **kwargs):
        super(PositionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({'class': 'form-control'})


class GroupForm(forms.ModelForm):
    class Meta:
        
        fields = ['name']

