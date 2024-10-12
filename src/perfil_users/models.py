from django.db import models
from django.contrib.auth.models import User


class Position(models.Model):
    position = models.CharField(max_length=150, verbose_name='Posição')
    description = models.TextField(blank=True, verbose_name='Descrição do cargo')

    def __str__(self) -> str:
        return self.position


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    position = models.ForeignKey(Position, on_delete=models.CASCADE, verbose_name='Posição')
    birth = models.DateField()
    description = models.TextField(blank=True, verbose_name='Descrição do Funcionario')

    def __str__(self) -> str:
        return f'{self.user}'