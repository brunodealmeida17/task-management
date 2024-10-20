# Generated by Django 5.1.2 on 2024-10-19 02:47

import ckeditor_uploader.fields
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Nome da tarefa')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='descrição da tarefa')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Data da criaçao da tarefa')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
        ),
        migrations.CreateModel(
            name='TimeEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Data de inicio da tarefa')),
                ('estimated_time', models.CharField(max_length=20, verbose_name='estimativa do tempo')),
                ('description', ckeditor_uploader.fields.RichTextUploadingField(blank=True, verbose_name='descrição do que foi feito na tarefa')),
                ('status', models.CharField(choices=[('pendente', 'Pendente'), ('em_andamento', 'Em Andamento'), ('feito', 'Feito'), ('reavaliar', 'Reavaliar')], default='pendente', max_length=20, verbose_name='Status')),
                ('task', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='task', to='tasks.task', verbose_name='Tarefa realcionada')),
            ],
            options={
                'verbose_name': 'Entrada de tempo',
            },
        ),
    ]
