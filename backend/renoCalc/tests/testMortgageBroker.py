from django.db import IntegrityError
from django.test import TestCase
from renoCalc.models import ContractorModel, MortgageBrokerModel
from django.core.management import call_command


class MortgageBrokerTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)
        self.contractorWithAllFields = ContractorModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        self.contractorWithAllFields.full_clean()
        self.contractorWithAllFields.save()
        self.assertTrue(ContractorModel.objects.filter(name="John Doe").exists())

    def testMortgageBrokerWithContractorMade(self):
        MortgageBrokerServiceWithAllFields = MortgageBrokerModel.objects.create(
            contractor=self.contractorWithAllFields,
            description="test",
            financeMinimum=10,
            commission={
                "Home": {"lendingFees": 1, "interest": 5},
                "Construction": {"lendingFees": 2, "interest": 10},
            },
        )
        self.assertTrue(MortgageBrokerModel.objects.filter(description="test").exists())

    def testMortgageBrokerWithoutNecessaryField(self):
        with self.assertRaises(IntegrityError):
            MortgageBrokerServiceWithSomeFields = MortgageBrokerModel.objects.create(
                contractor=self.contractorWithAllFields,
                description="test",
                commission={
                    "Home": {"lendingFees": 1, "interest": 5},
                    "Construction": {"lendingFees": 2, "interest": 10},
                },
            )
            self.assertTrue(MortgageBrokerModel.objects.filter(description="test").exists())
