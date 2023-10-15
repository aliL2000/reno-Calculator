from django.test import TestCase
from application.models import User
from django.core.exceptions import ValidationError
from django.core.management import call_command

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
        # Verify that the User just made exists within the DB
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyEmailProvided(self):
        userWithOnlyEmail = User.objects.create(
            name="John Doe", email="johndoe@example.com", address="123 Main St"
        )
        userWithOnlyEmail.full_clean()
        userWithOnlyEmail.save()
        # Verify that a User exists with only their email provided
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testCreateUserWithOnlyPhoneNumberProvided(self):
        userWithOnlyPhoneNumber = User.objects.create(
            name="John Doe", phoneNumber="1234567890", address="123 Main St"
        )
        userWithOnlyPhoneNumber.full_clean()
        userWithOnlyPhoneNumber.save()
        # Verify that a User exists with only their phone number provided
        self.assertTrue(User.objects.filter(name="John Doe").exists())

    def testUserCreationWithNoPhoneNumberOrEmailProvided(self):
        # Verify that a Validation Error has occured when attempting to create a User without any Phone Number/Email
        with self.assertRaises(ValidationError):
            userWithNoPhoneNumberOrEmail = User.objects.create(
                name="John Doe", address="123 Main St"
            )
            userWithNoPhoneNumberOrEmail.full_clean()

    def testUserCreationWithNoFieldsProvided(self):
        # Verify that a Validation Error has occured when a User with NO fields is attempted to be created
        with self.assertRaises(ValidationError):
            userWithNoFields = User.objects.create()
            userWithNoFields.full_clean()
