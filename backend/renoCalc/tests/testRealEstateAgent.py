from django.test import TestCase
from renoCalc.models import Contractor,RealEstateAgent
from django.core.exceptions import ValidationError
from django.core.management import call_command


class RealEstateAgentTestCases(TestCase):
    contractorWithAllFields = None


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

    def testRealEstateAgentWithContractorMade(self):
        # Initialize the contractor and save the DB
        #Verify that contractor exists within the DB
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())
        laundryApplianceServiceWithAllFields = RealEstateAgent.objects.create(
            contractor=self.contractorWithAllFields,
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