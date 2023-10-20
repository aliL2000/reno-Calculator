from django.test import TestCase
from renoCalc.models import UserModel
from django.core.exceptions import ValidationError
from django.core.management import call_command

class UserTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testCreateUserWithAllFieldsProvided(self):
        userWithAllFields = UserModel.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
        )
        userWithAllFields.full_clean()
        userWithAllFields.save()
        # Verify that the User just made exists within the DB
        self.assertTrue(UserModel.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyEmailProvided(self):
        userWithOnlyEmail = UserModel.objects.create(
            name="John Doe", email="johndoe@example.com", address="123 Main St"
        )
        userWithOnlyEmail.full_clean()
        userWithOnlyEmail.save()
        # Verify that a User exists with only their email provided
        self.assertTrue(UserModel.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyPhoneNumberProvided(self):
        userWithOnlyPhoneNumber = UserModel.objects.create(
            name="John Doe", phoneNumber="1234567890", address="123 Main St"
        )
        userWithOnlyPhoneNumber.full_clean()
        userWithOnlyPhoneNumber.save()
        # Verify that a User exists with only their phone number provided
        self.assertTrue(UserModel.objects.filter(name="John Doe").exists())

    def testUserCreationWithNoPhoneNumberOrEmailProvided(self):
        # Verify that a Validation Error has occured when attempting to create a User without any Phone Number/Email
        with self.assertRaises(ValidationError):
            userWithNoPhoneNumberOrEmail = UserModel.objects.create(
                name="John Doe", address="123 Main St"
            )
            userWithNoPhoneNumberOrEmail.full_clean()

    def testUserCreationWithNoFieldsProvided(self):
        # Verify that a Validation Error has occured when a User with NO fields is attempted to be created
        with self.assertRaises(ValidationError):
            userWithNoFields = UserModel.objects.create()
            userWithNoFields.full_clean()
