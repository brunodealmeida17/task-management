from django.apps import AppConfig


class PerfilUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'perfil_users'

    def ready(self):
        import perfil_users.signals 
