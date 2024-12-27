from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Convierte un usuario en administrador'

    def add_arguments(self, parser):
        parser.add_argument('username', type=str, help='El nombre de usuario a convertir en administrador')

    def handle(self, *args, **kwargs):
        username = kwargs['username']
        try:
            user = User.objects.get(username=username)
            user.is_staff = True
            user.is_superuser = True
            user.save()
            self.stdout.write(self.style.SUCCESS(f"El usuario '{username}' ahora es administrador."))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR(f"El usuario '{username}' no existe."))
