from django.apps import AppConfig


class MpesaConfig(AppConfig):
    name = 'mpesa'
    
    def ready(self):
        from mpesa import signals

        pass
