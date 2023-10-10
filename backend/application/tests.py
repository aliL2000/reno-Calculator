from django.test import TestCase
from application.models import User, Contractor
from django.core.exceptions import ValidationError

#TESTING USER CLASS
class UserTestCases(TestCase):

    def setUp(self):
        # Clear the database by flushing it
        self._reset_database()

    def _reset_database(self):
        # This function clears the database by flushing it
        from django.core.management import call_command
        call_command('flush', interactive=False)


    def testCreateUserWithAllFieldsProvided(self):
        userWithAllFields = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St"
        )
        userWithAllFields.full_clean()
        userWithAllFields.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())
            
    def testCreateUserWithOnlyEmailProvided(self):
        userWithOnlyEmail = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            address="123 Main St"
        )
        userWithOnlyEmail.full_clean()
        userWithOnlyEmail.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())   

    def testCreateUserWithOnlyPhoneNumberProvided(self):
        userWithOnlyPhoneNumber = User.objects.create(
            name="John Doe",
            phoneNumber="1234567890",
            address="123 Main St"
        )
        userWithOnlyPhoneNumber.full_clean()
        userWithOnlyPhoneNumber.save()
        self.assertTrue(User.objects.filter(name="John Doe").exists())     

    def testUserCreationWithNoPhoneNumberOrEmailProvided(self):
        #This test's checks to see when attempting to submit a user with no email or phone number, the clean method should create a Validation Error
        with self.assertRaises(ValidationError):
            userWithNoPhoneNumberOrEmail = User.objects.create(
                name="John Doe",
                address="123 Main St"
            )
            userWithNoPhoneNumberOrEmail.full_clean()