from django.db import IntegrityError
from django.test import TestCase
from renoCalc.models import Contractor, RealEstateLaywer
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

    def testRealEstateLawyerWithContractorMade(self):
        commission_data = {2.5: 1_000_000, 2: 500_000, 1.5: 200_000}
        RealEstateLawyerServiceWithAllFields = RealEstateLaywer.objects.create(
            contractor=self.contractorWithAllFields,
            description="testing",
            commission=commission_data,
        )

        self.assertTrue(RealEstateLaywer.objects.filter(description="testing").exists())

    def testRealEstateLawyerWithoutNecessaryField(self):
        with self.assertRaises(IntegrityError):
            RealEstateLawyerServiceWithSomeFields = RealEstateLaywer.objects.create(
                contractor=self.contractorWithAllFields,
                description="test",
            )
            self.assertTrue(RealEstateLaywer.objects.filter(description="test").exists())