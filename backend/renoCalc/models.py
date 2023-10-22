import decimal
from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import AbstractUser


class UserModel(AbstractUser):
    username = models.CharField(max_length=100, unique=True, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} - {self.email}"


class UserHomeAndRenovationConfigurationModel(models.Model):
    user = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    uniqueConfiguration = models.JSONField()


class ContractorModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    website_link = models.URLField(max_length=200, blank=True, null=True)
    rating = models.DecimalField(
        max_digits=2,
        decimal_places=1,
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class PropertyTypeModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


class RegionModel(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"


# Below are services, will be expanding as we add more and more of these services.


class RealEstateAgentModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    typeOfWork = models.ManyToManyField(PropertyTypeModel)
    regions = models.ManyToManyField(RegionModel)
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class MortgageBrokerModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    financeMinimum = models.IntegerField()
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class RealEstateLaywerModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class HomeInspectorModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class SurveyorModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class ArchitectModel(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    description = models.TextField()
    commission = models.JSONField()

    def __str__(self):
        return f"{self.contractor} - {self.description}"


class LaundryAppliances(models.Model):
    contractor = models.ForeignKey(ContractorModel, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    choice = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    # Cost of Material and Cost of Labour

    def __str__(self):
        return f"{self.contractor} - {self.service} - {self.choice}"


@receiver(pre_save, sender=LaundryAppliances)
def ensure_contractor_exists(sender, instance, **kwargs):
    # Check if the contractor already exists
    try:
        ContractorModel.objects.get(name=instance.contractor.name)
    except ContractorModel.DoesNotExist:
        # Contractor does not exist, prevent saving the LaundryAppliances instance
        raise Exception(
            "Contractor does not exist, ensure the contractor exists before saving"
        )


# class Framers(models.Model):
#     contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
#     subCategory = models.CharField(max_length=100)
#     materialCost = JSONField()
#     labourCost = ArrayField(models.CharField(max_length=200), blank=True)


# import math

# # Your input dictionary with integer values and an indicator
# data = {
#     'A': (25, True),  # The second element of the tuple is the indicator
#     'B': (1.5, False),  # This value won't be rounded
#     'concrete': (50, True),
# }

# data = {
#     'floor': (25, True),  # The second element of the tuple is the indicator
#     'wall': (1.5, False),  # This value won't be rounded
#     'concrete': (50, True),
# }
# # Rounding factor (e.g., rounding up to the nearest multiple)
# rounding_factor = 11
# print(type(data2))
# if data2[1]!=0 and rounding_factor < data2[1]:
#     value = data2[1]
# else:
#     value = rounding_factor*data2[0]
# print(value)


# # Round up the values in the dictionary based on the indicator
# rounded_data = {}
# for key, (value, round_flag) in data.items():
#     if round_flag:
#         rounded_value = math.ceil(rounding_factor/value) * value
#     else:
#         rounded_value = value * rounding_factor
#     rounded_data[key] = rounded_value

# # Display the rounded data
# for key, value in rounded_data.items():
#     print(f"{key}: {value}")
