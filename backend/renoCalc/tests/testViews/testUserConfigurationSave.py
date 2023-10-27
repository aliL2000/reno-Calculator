from django.test import TestCase
from django.urls import reverse
from renoCalc.models import UserModel, UserHomeAndRenovationConfigurationModel
from django.core.management import call_command


class MyViewTestCase(TestCase):
    def setUp(self):
        self.json_data = '{"key": "value"}'

        call_command("flush", interactive=False)
        self.userWithAllFields = UserModel.objects.create(
            first_name="John",
            last_name="Doe",
            email="johndoe@example.com",
            phoneNumber="1234567890",
            address="123 Main St",
            password="jdoe098",
        )

        self.userWithAllFields.full_clean()
        self.userWithAllFields.save()
        self.assertTrue(UserModel.objects.filter(first_name="John").exists())

    def test_my_view(self):
        url = reverse(
            "saveUserConfiguration", kwargs={"userID": self.userWithAllFields.id}
        )
        response = self.client.post(
            url, data=self.json_data, content_type="application/json"
        )

        self.assertEqual(response.status_code, 200)

        dbUserConfigurationInstance = (
            UserHomeAndRenovationConfigurationModel.objects.filter(
                user=self.userWithAllFields
            )
        )
        self.assertTrue(dbUserConfigurationInstance.exists())
