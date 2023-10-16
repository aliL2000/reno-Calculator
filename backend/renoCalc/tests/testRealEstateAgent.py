from django.test import TestCase
from renoCalc.models import Contractor, RealEstateAgent, PropertyTypeModel, RegionModel
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
        self.property_type1 = PropertyTypeModel.objects.create(name="Semi-Detached")
        self.property_type2 = PropertyTypeModel.objects.create(name="Townhouse")
        self.property_type3 = PropertyTypeModel.objects.create(name="Detached")
        self.regions_type1 = RegionModel.objects.create(name="Toronto")
        self.regions_type1 = RegionModel.objects.create(name="Richmond Hill")

    def testRealEstateAgentWithContractorMade(self):
        commission_data = {2.5: 1_000_000, 2: 500_000, 1.5: 200_000}
        RealEstateAgentServiceWithAllFields = RealEstateAgent.objects.create(
            contractor=self.contractorWithAllFields,
            description="testing",
            commission=commission_data
        )

        
        RealEstateAgentServiceWithAllFields.typeOfWork.add(self.property_type1)
        RealEstateAgentServiceWithAllFields.regions.add(self.regions_type1)
        # Verify that the service was made with the given contractor
        self.assertTrue(RealEstateAgent.objects.filter(description="testing").exists())
