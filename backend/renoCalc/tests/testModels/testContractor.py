from django.test import TestCase
from renoCalc.models import ContractorModel
from django.core.exceptions import ValidationError
from django.core.management import call_command


class ContractorTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testContractorWithAllFieldsProvided(self):
        contractorWithAllFields = ContractorModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        contractorWithAllFields.full_clean()
        contractorWithAllFields.save()
        #Verify that a contractor with ALL fields has been created
        self.assertTrue(ContractorModel.objects.filter(name="John Doe").exists())

    def testContractorWithNoWebsiteProvided(self):
        contractorWithNoWebsite = ContractorModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
        )
        contractorWithNoWebsite.full_clean()
        contractorWithNoWebsite.save()
        #Verify that a ContractorModel can exist WITHOUT a website
        self.assertTrue(ContractorModel.objects.filter(name="John Doe").exists())

    def testContractorWithNoNameProvided(self):
        #Verify that a Validation Error occurs when not supplying a necessary field
        with self.assertRaises(ValidationError):
            contractorWithNoName = ContractorModel.objects.create(
                email="johndoe@example.com",
                phoneNumber="1234567890",
                address="123 Main St",
                website_link="https://test.com",
            )
            contractorWithNoName.full_clean()

    def testContractorWithNoFieldsProvided(self):
        #Verify that a Validation Error occurs when not ANY field
        with self.assertRaises(ValidationError):
            contractorWithNoFieldsProvided = ContractorModel.objects.create()
            contractorWithNoFieldsProvided.full_clean()