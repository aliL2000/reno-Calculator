from django.db import IntegrityError
from django.test import TestCase
from renoCalc.models import Contractor, HomeInspector
from django.core.management import call_command


class HomeInspectorTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)
        self.contractorWithAllFields = Contractor.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        self.contractorWithAllFields.full_clean()
        self.contractorWithAllFields.save()
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())

    def testHomeInspectorWithContractorMade(self):
        commission_data = {"Home": 1_000_000, "Detached": 500_000, "Semi": 200_000}
        HomeInspectorServiceWithAllFields = HomeInspector.objects.create(
            contractor=self.contractorWithAllFields,
            description="testing",
            commission=commission_data,
        )

        self.assertTrue(HomeInspector.objects.filter(description="testing").exists())

    def testHomeInspectorrWithoutNecessaryField(self):
        with self.assertRaises(IntegrityError):
            HomeInspectorServiceWithSomeFields = HomeInspector.objects.create(
                contractor=self.contractorWithAllFields,
                description="test",
            )
            self.assertTrue(HomeInspector.objects.filter(description="test").exists())
