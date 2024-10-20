# seu_app/signals.py

from django.contrib.auth.models import Group
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_groups(sender, **kwargs):
    if sender.name == 'perfil_users':
        group_names = ['tasks', 'users', 'timeEntry', 'None']
        for name in group_names:
            Group.objects.get_or_create(name=name)
