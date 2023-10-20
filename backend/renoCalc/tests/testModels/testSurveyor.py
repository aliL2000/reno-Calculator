from django.db import IntegrityError
from django.test import TestCase
from renoCalc.models import ContractorModel, SurveyorModel
from django.core.management import call_command


class SurveyorTestCases(TestCase):
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

    def testSurveyorWithContractorMade(self):
        commission_data = {"Home": 1_000_000, "Detached": 500_000, "Semi": 200_000}
        SurveyorServiceWithAllFields = SurveyorModel.objects.create(
            contractor=self.contractorWithAllFields,
            description="testing",
            commission=commission_data,
        )

        self.assertTrue(SurveyorModel.objects.filter(description="testing").exists())

    def testSurveyorWithoutNecessaryField(self):
        with self.assertRaises(IntegrityError):
            SurveyorServiceWithSomeFields = SurveyorModel.objects.create(
                contractor=self.contractorWithAllFields,
                description="test",
            )
            self.assertTrue(SurveyorModel.objects.filter(description="test").exists())
