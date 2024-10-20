from perfil_users.models import CustomUser
import re
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Task(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='tasks', verbose_name="Usuario")
    name = models.CharField(max_length=200, verbose_name='Nome da tarefa')
    description = RichTextUploadingField(blank=True, verbose_name='descrição da tarefa')
    created_at = models.DateField(auto_now_add=True, verbose_name='Data da criaçao da tarefa')


    def __str__(self) -> str:
        return self.name

    
class TimeEntry(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_andamento', 'Em Andamento'),
        ('feito', 'Feito'),
        ('reavaliar', 'Reavaliar'),
    ]
    task = models.OneToOneField(Task, on_delete=models.CASCADE, related_name="task", verbose_name='Tarefa realcionada')
    date = models.DateField(verbose_name='Data de inicio da tarefa')
    estimated_time = models.CharField(max_length=20, verbose_name='estimativa do tempo')
    description = RichTextUploadingField(blank=True, verbose_name='descrição do que foi feito na tarefa')
    status = status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name="Status"
    )

    def __str__(self) -> str:
        return f"{self.task.name} - {self.estimated_time}"
    
    class Meta:
        verbose_name = "Entrada de tempo"


    @property
    def hours_estimated(self):
        """
            Converts the value of `estimated_time` from a flexible format (e.g., `1w 3d 2h 45m`, `3h 30m`, `45m`, `1d`)
            into a numerical value in hours.

            :return: returns the rounded value in hours
        """
        pattern = re.compile(r'(?:(\d+)w)?\s*(?:(\d+)d)?\s*(?:(\d+)h)?\s*(?:(\d+)m)?')
        match = pattern.search(self.estimated_time)

        if not match:
            return 0

        weeks = match.group(1)  # Weeks
        days = match.group(2)   # Days
        hours = match.group(3)  # Hours
        minutes = match.group(4)  # Minutes

        total_hours = 0

        if weeks:
            total_hours += int(weeks) * 44  # Converts weeks to hours (1 week = 7 days = 44 working hours)
        if days:
            total_hours += int(days) * 8  # Converts days to hours (1 day = 8 working hours)
        if hours:
            total_hours += int(hours)  # Direct hours
        if minutes:
            total_hours += int(minutes) / 60  # Converts minutes to hours (1 hour = 60 minutes)

        return round(total_hours, 2)

    


