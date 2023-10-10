from django.test import TestCase
from application.models import User, Contractor
from django.core.exceptions import ValidationError

#TESTING USER CLASS
class UserTestCases(TestCase):
    def test_create_user_with_all_fields(self):
        user_with_all_fields = User.objects.create(
            name="JohnDoe1",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St"
        )
        user_with_all_fields_exists = User.objects.filter(name="JohnDoe1").exists()
        self.assertTrue(user_with_all_fields_exists)
            
    def test_create_user_with_only_email_provided(self):
        user_with_only_email = User.objects.create(
            name="JohnDoe2",
            email="johndoe@example.com",
            address="123 Main St"
        )
        user_with_only_email_exists = User.objects.filter(name="JohnDoe2").exists()
        self.assertTrue(user_with_only_email_exists)   

    def test_create_user_with_only_phone_number_provided(self):
        userWithOnlyPhoneNumber = User.objects.create(
            name="JohnDoe3",
            phoneNumber="1234567890",
            address="123 Main St"
        )
        userWithOnlyPhoneNumber.full_clean()
        userWithOnlyPhoneNumber.save()
        self.assertTrue(User.objects.filter(name="JohnDoe3").exists())     

    def testUserCreationWithNoPhoneNumberOrEmail(self):

        with self.assertRaises(ValidationError):
            userWithNoPhoneNumberOrEmail = User.objects.create(
                name="JohnDoe4",
                address="123 Main St"
            )
            userWithNoPhoneNumberOrEmail.full_clean()