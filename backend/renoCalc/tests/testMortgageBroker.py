from django.db import IntegrityError
from django.test import TestCase
from renoCalc.models import Contractor, MortgageBroker
from django.core.management import call_command


class RealEstateAgentTestCases(TestCase):
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

    def testMortgageBrokerWithContractorMade(self):
        MortgageBrokerServiceWithAllFields = MortgageBroker.objects.create(
            contractor=self.contractorWithAllFields,
            description="test",
            financeMinimum=10,
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        self.assertTrue(MortgageBroker.objects.filter(description="test").exists())

    def testMortgageBrokerWithContractorMade(self):
        with self.assertRaises(IntegrityError):
            MortgageBrokerServiceWithAllFields = MortgageBroker.objects.create(
                contractor=self.contractorWithAllFields,
                description="test",
                commission={
                    "Home": {"lendingFees": 1, "interest": 5},
                    "Construction": {"lendingFees": 2, "interest": 10},
                },
            )
            self.assertTrue(MortgageBroker.objects.filter(description="test").exists())
