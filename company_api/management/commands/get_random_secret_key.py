from django.core.management.utils import get_random_secret_key
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        secret_key = get_random_secret_key()
        text = 'SECRET_KEY = \'{0}\''.format(secret_key)
        print(text)