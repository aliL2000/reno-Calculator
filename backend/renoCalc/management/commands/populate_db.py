from django.core.management.base import BaseCommand
from renoCalc.models import UserModel  # Import the model you want to populate

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        # Your code to populate the database goes here
        UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
            username="jdoemain",
        )
        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))