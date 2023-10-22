from django.core.management.base import BaseCommand
from renoCalc.models import UserModel, ContractorModel

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **options):
        #CREATE USERS
        UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
            username="jdoemain",
        )
        UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe2@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe0981",
        )
        UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
            username="jdoemain2",
        )

        #CREATE CONTRACTORS
        ContractorModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
            rating = 1.5
        )
        ContractorModel.objects.create(
            name="John Doe2",
            email="johndoe2@example.com",
            phoneNumber="12345678901",
            address="1231 Main St",
            rating = 2.5
        )

        self.stdout.write(self.style.SUCCESS('Database populated successfully!'))