from django.apps import AppConfig


class AuthenticationConfig(AppConfig):
    name = 'authentication'
    verbose_name = 'authentication'

    def ready(self):
        import authentication.signals  # pragma: no flakes
