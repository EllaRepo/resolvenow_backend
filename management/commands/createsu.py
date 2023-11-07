# images/management/commands/createsu.py

from django.contrib.auth.models import User
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Creates a superuser.'

    def handle(self, *args, **options):
        if not User.objects.filter(email='admin@resolvenow.com').exists():
            User.objects.create_superuser(
                email='admin@resolvenow.com',
                password='resolvenowadmin'
            )
        print('Superuser has been created.')