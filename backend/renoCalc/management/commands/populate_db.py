from django.core.management.base import BaseCommand
from renoCalc.models import (
    UserModel,
    ContractorModel,
    RealEstateAgentModel,
    PropertyTypeModel,
    RegionModel,
    MortgageBrokerModel,
    RealEstateLaywerModel,
    HomeInspectorModel,
    SurveyorModel,
    ArchitectModel,
)

#TO RUN:
#python manage.py populate_db


class Command(BaseCommand):
    help = "Populate the database with sample data"

    def handle(self, *args, **options):
        # CREATE USERS
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

        # CREATE CONTRACTORS
        ct1 = ContractorModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
            rating=1.5,
        )
        ct2 = ContractorModel.objects.create(
            name="John Doe2",
            email="johndoe2@example.com",
            phoneNumber="12345678901",
            address="1231 Main St",
            rating=2.5,
        )
        ct3 = ContractorModel.objects.create(
            name="John Doe3",
            email="johndoe@example.com",
            phoneNumber="12345678902",
            address="1232 Main St",
            website_link="https://test.com",
            rating=3.5,
        )

        # CREATE REALESTATEAGENTS
        self.property_type1 = PropertyTypeModel.objects.create(name="Semi-Detached")
        self.property_type2 = PropertyTypeModel.objects.create(name="Townhouse")
        self.property_type3 = PropertyTypeModel.objects.create(name="Detached")
        self.regions_type1 = RegionModel.objects.create(name="Toronto")
        self.regions_type2 = RegionModel.objects.create(name="Richmond Hill")
        rta1 = RealEstateAgentModel.objects.create(
            contractor=ct1,
            description="testing",
            commission={2.5: 1_000_000, 2: 500_000, 1.5: 200_000},
        )
        rta2 = RealEstateAgentModel.objects.create(
            contractor=ct3,
            description="testing",
            commission={2.5: 1_000_000, 2: 500_000, 1.5: 200_000},
        )
        rta1.typeOfWork.add(self.property_type1)
        rta1.regions.add(self.regions_type1)
        rta2.typeOfWork.add(self.property_type2, self.property_type3)
        rta2.regions.add(self.regions_type1, self.regions_type2)

        # CREATE MORTGAGE BROKER MODEL
        MortgageBrokerModel.objects.create(
            contractor=ct1,
            description="test",
            financeMinimum=10,
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        MortgageBrokerModel.objects.create(
            contractor=ct3,
            description="test",
            financeMinimum=10,
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )

        # CREATEREALESTATELAYWER
        RealEstateLaywerModel.objects.create(
            contractor=ct1,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        RealEstateLaywerModel.objects.create(
            contractor=ct2,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        # TODO:CREATEHOMEINSPECTOR
        HomeInspectorModel.objects.create(
            contractor=ct3,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        HomeInspectorModel.objects.create(
            contractor=ct2,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        HomeInspectorModel.objects.create(
            contractor=ct1,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        # TODO:CREATESURVEYOR
        SurveyorModel.objects.create(
            contractor=ct1,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        SurveyorModel.objects.create(
            contractor=ct2,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        # TODO:CREATEARCHITECT
        ArchitectModel.objects.create(
            contractor=ct3,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        ArchitectModel.objects.create(
            contractor=ct1,
            description="test",
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        self.stdout.write(self.style.SUCCESS("Database populated successfully!"))
