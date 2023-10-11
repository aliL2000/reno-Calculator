from django.test import TestCase
from application.models import User, Contractor, LaundryAppliances
from django.core.exceptions import ValidationError
from django.core.management import call_command


# TESTING USER CLASS
class UserTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testCreateUserWithAllFieldsProvided(self):
        userWithAllFields = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
        )
        userWithAllFields.full_clean()
        userWithAllFields.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyEmailProvided(self):
        userWithOnlyEmail = User.objects.create(
            name="John Doe", email="johndoe@example.com", address="123 Main St"
        )
        userWithOnlyEmail.full_clean()
        userWithOnlyEmail.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyPhoneNumberProvided(self):
        userWithOnlyPhoneNumber = User.objects.create(
            name="John Doe", phoneNumber="1234567890", address="123 Main St"
        )
        userWithOnlyPhoneNumber.full_clean()
        userWithOnlyPhoneNumber.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testUserCreationWithNoPhoneNumberOrEmailProvided(self):
        # This test checks to see when attempting to submit a user with no email or phone number, the clean method should create a Validation Error
        with self.assertRaises(ValidationError):
            userWithNoPhoneNumberOrEmail = User.objects.create(
                name="John Doe", address="123 Main St"
            )
            userWithNoPhoneNumberOrEmail.full_clean()

    def testUserCreationWithNoFieldsProvided(self):
        with self.assertRaises(ValidationError):
            userWithNoFields = User.objects.create()
            userWithNoFields.full_clean()


# TESTING CONTRACTOR CLASS
class ContractorTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testContractorWithAllFieldsProvided(self):
        contractorWithAllFields = Contractor.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        contractorWithAllFields.full_clean()
        contractorWithAllFields.save()
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())

    def testContractorWithNoWebsiteProvided(self):
        contractorWithNoWebsite = Contractor.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
        )
        contractorWithNoWebsite.full_clean()
        contractorWithNoWebsite.save()
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())

    def testContractorWithNoNameProvided(self):
        with self.assertRaises(ValidationError):
            contractorWithNoName = Contractor.objects.create(
                email="johndoe@example.com",
                phoneNumber="1234567890",
                address="123 Main St",
                website_link="https://test.com",
            )
            contractorWithNoName.full_clean()

    def testContractorWithNoFieldsProvided(self):
        with self.assertRaises(ValidationError):
            contractorWithNoFieldsProvided = Contractor.objects.create()
            contractorWithNoFieldsProvided.full_clean()


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
        self.assertTrue(Contractor.objects.filter(name="John Doe").exists())
        laundryApplianceServiceWithAllFields = LaundryAppliances.objects.create(
            contractor=contractorWithAllFields,
            service="Washing Machine",
            choice="Top Load",
            cost=1000,
        )
        self.assertTrue(
            LaundryAppliances.objects.filter(
                service="Washing Machine", choice="Top Load"
            ).exists()
        )

    def testLaundryApplianceWithContractorNotMade(self):
        # Initialize the contractor and save the DB
        contractorWithAllFields = Contractor(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            website_link="https://test.com",
        )
        self.assertFalse(Contractor.objects.filter(name="John Doe").exists())

        with self.assertRaises(Exception):
            laundryApplianceServiceWithAllFields = LaundryAppliances.objects.create(
                contractor=contractorWithAllFields,
                service="Washing Machine",
                choice="Top Load",
                cost=1000,
            )
