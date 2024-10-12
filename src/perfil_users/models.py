from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission

class Position(models.Model):
    position = models.CharField(max_length=150, verbose_name='Posição')
    description = models.TextField(blank=True, verbose_name='Descrição do cargo')

    def __str__(self) -> str:
        return self.position


class CustomUser(AbstractUser):    
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Posição', null=True, blank=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    birth = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, verbose_name='Descrição do Funcionario')
