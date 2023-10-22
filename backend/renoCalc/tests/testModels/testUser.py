from django.test import TestCase
from renoCalc.models import UserModel
from django.core.exceptions import ValidationError
from django.core.management import call_command


class UserTestCases(TestCase):
    def setUp(self):
        call_command("flush", interactive=False)

    def testCreateUserWithAllFieldsProvided(self):
        userWithAllFields = UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
            username="jdoemain",
        )
        userWithAllFields.full_clean()
        userWithAllFields.save()
        # Verify that the User just made exists within the DB
        self.assertTrue(UserModel.objects.filter(first_name="John").exists())

    def testCreateUserWithOnlyEmailProvided(self):
        userWithOnlyEmail = UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
        )
        userWithOnlyEmail.full_clean()
        userWithOnlyEmail.save()
        # Verify that a User exists with only their email provided
        self.assertTrue(UserModel.objects.filter(first_name="John").exists())

    def testCreateUserWithOnlyUsernameProvided(self):
        userWithOnlyUsername = UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
            username="jdoemain",
        )
        userWithOnlyUsername.full_clean()
        userWithOnlyUsername.save()
        # Verify that a User exists with only their phone number provided
        self.assertTrue(UserModel.objects.filter(first_name="John").exists())

    def testUserCreationWithNoEmailOrUsernameProvided(self):
        # Verify that a Validation Error has occured when a User with NO fields is attempted to be created
        with self.assertRaises(ValidationError):
            userWithNoFields = UserModel.objects.create(
                first_name="John",
                last_name="Doe",
                phoneNumber="1234567890",
                address="123 Main St",
                password="jdoe098",
            )
            userWithNoFields.full_clean()

    def testUserCreationWithNoFieldsProvided(self):
        # Verify that a Validation Error has occured when a User with NO fields is attempted to be created
        with self.assertRaises(ValidationError):
            userWithNoFields = UserModel.objects.create()
            userWithNoFields.full_clean()
