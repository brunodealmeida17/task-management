from django.contrib.auth.models import User
from perfil_users.models import Profile
import re
from django.db import models
from datetime import timedelta, date


class Task(models.Model):
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='tasks')
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateField(auto_now_add=True)


    def __str__(self) -> str:
        return self.name

    
class TimeEntry(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name="task")
    date = models.DateField()
    estimated_time = models.CharField(max_length=20)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f"{self.task.name} - {self.estimated_time}"


    @property
    def hours_estimated(self):
        """
        Converte o valor de `estimated_time` no formato flexível (e.g., `1w 3d 2h 45m`, `3h 30m`, `45m`, `1d`)
        para um valor numérico de horas.

        :return: retorna o valor arredondado em horas
        """
        pattern = re.compile(r'(?:(\d+)w)?\s*(?:(\d+)d)?\s*(?:(\d+)h)?\s*(?:(\d+)m)?')
        match = pattern.search(self.estimated_time)

        if not match:
            return 0
        
        weeks = match.group(1)  # Semanas
        days = match.group(2)   # Dias
        hours = match.group(3)  # Horas
        minutes = match.group(4)  # Minutos

        total_hours = 0

        if weeks:
            total_hours += int(weeks) * 168  # Converte semanas para horas (1 semana = 7 dias = 168 horas)
        if days:
            total_hours += int(days) * 24  # Converte dias para horas (1 dia = 24 horas)
        if hours:
            total_hours += int(hours)  # Horas diretas
        if minutes:
            total_hours += int(minutes) / 60  # Converte minutos para horas (1 hora = 60 minutos)

        return round(total_hours, 2)
    


