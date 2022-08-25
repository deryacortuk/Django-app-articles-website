from django.apps import AppConfig



class ProfilConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'Profil'
    
    def ready(self):
        import Profil.signals