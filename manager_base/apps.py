from django.apps import AppConfig


class ManagerBaseConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'manager_base'
