from django.test import TestCase
from application.models import Contractor, LaundryAppliances
from django.core.management import call_command

class LaundryApplianceTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testLaundryApplianceWithContractorMade(self):
        # Initialize the contractor and save the DB
        contractorWithAllFields = Contractor.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        contractorWithAllFields.full_clean()
        contractorWithAllFields.save()
        #Verify that contractor exists within the DB
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())
        laundryApplianceServiceWithAllFields = LaundryAppliances.objects.create(
            contractor=contractorWithAllFields,
            service="Washing Machine",
            choice="Top Load",
            cost=1000,
        )
        #Verify that the service was made with the given contractor
        self.assertTrue(
            LaundryAppliances.objects.filter(
                service="Washing Machine", choice="Top Load"
            ).exists()
        )

    def testLaundryApplianceWithContractorNotMade(self):
        # Initialize a contractor, but DO NOT save to the DB.
        contractorWithAllFields = Contractor(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        #Verify that the contractor DOES NOT exist within the DB
        self.assertFalse(Contractor.objects.filter(name="John Doe").exists())

        #Verify that the BE raises an exception when attempting to create a non-saved Contractor
        with self.assertRaises(Exception):
            laundryApplianceServiceWithAllFields = LaundryAppliances.objects.create(
                contractor=contractorWithAllFields,
                service="Washing Machine",
                choice="Top Load",
                cost=1000,
            )
