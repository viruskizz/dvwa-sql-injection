from django.apps import AppConfig


class PgsqlConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'pgsql'
    label = 'pgsql'
