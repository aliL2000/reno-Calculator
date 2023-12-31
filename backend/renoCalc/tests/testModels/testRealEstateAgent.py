from django.test import TestCase
from renoCalc.models import ContractorModel, RealEstateAgentModel, PropertyTypeModel, RegionModel
from django.core.management import call_command


class RealEstateAgentTestCases(TestCase):
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
        self.property_type1 = PropertyTypeModel.objects.create(name="Semi-Detached")
        self.property_type2 = PropertyTypeModel.objects.create(name="Townhouse")
        self.property_type3 = PropertyTypeModel.objects.create(name="Detached")
        self.regions_type1 = RegionModel.objects.create(name="Toronto")
        self.regions_type2 = RegionModel.objects.create(name="Richmond Hill")

    def testRealEstateAgentWithContractorMade(self):
        commission_data = {2.5: 1_000_000, 2: 500_000, 1.5: 200_000}
        RealEstateAgentServiceWithAllFields = RealEstateAgentModel.objects.create(
            contractor=self.contractorWithAllFields,
            description="testing",
            commission=commission_data,
        )

        RealEstateAgentServiceWithAllFields.typeOfWork.add(self.property_type1)
        RealEstateAgentServiceWithAllFields.regions.add(self.regions_type1)
        self.assertTrue(RealEstateAgentModel.objects.filter(description="testing").exists())

    def testRealEstateAgentWithMultiplePropertyTypesContractorMade(self):
        commission_data = {1_000_000: 2.5, 500_000: 2, 200_000: 1.5}
        RealEstateAgentServiceWithMultiplePropertyTypes = (
            RealEstateAgentModel.objects.create(
                contractor=self.contractorWithAllFields,
                description="testing",
                commission=commission_data,
            )
        )

        RealEstateAgentServiceWithMultiplePropertyTypes.typeOfWork.add(
            self.property_type1, self.property_type2
        )
        RealEstateAgentServiceWithMultiplePropertyTypes.regions.add(self.regions_type1)
        # Verify that the service was made with the given contractor
        self.assertTrue(RealEstateAgentModel.objects.filter(description="testing").exists())

    def testRealEstateAgentWithMultipleRegionTypesContractorMade(self):
        commission_data = {1_000_000: 2.5, 500_000: 2, 200_000: 1.5}
        RealEstateAgentServiceWithMultiplePropertyTypes = (
            RealEstateAgentModel.objects.create(
                contractor=self.contractorWithAllFields,
                description="testing",
                commission=commission_data,
            )
        )

        RealEstateAgentServiceWithMultiplePropertyTypes.typeOfWork.add(
            self.property_type2
        )
        RealEstateAgentServiceWithMultiplePropertyTypes.regions.add(
            self.regions_type1, self.regions_type2
        )
        # Verify that the service was made with the given contractor
        self.assertTrue(RealEstateAgentModel.objects.filter(description="testing").exists())
