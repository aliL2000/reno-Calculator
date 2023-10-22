from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Flushes the database and resets it to its initial state'

    def handle(self, *args, **kwargs):
        from django.core.management import call_command
        call_command('flush', interactive=False)
        self.stdout.write(self.style.SUCCESS('Database flushed successfully'))
