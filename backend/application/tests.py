from django.test import TestCase
from application.models import User, Contractor

#TESTING USER CLASS
class UserTestCases(TestCase):
    def test_create_user_with_all_fields(self):
        # Create a user with all fields supplied
        user = User.objects.create(
            name="John Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St"
        )

        # Query the database to check if the user was created
        user_exists = User.objects.filter(name="John Doe").exists()

        # Assert that the user was created successfully
        self.assertTrue(user_exists)

