from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.forms import JSONField
from django.contrib.postgres.fields import ArrayField

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    def clean(self):
        super().clean()
        if self.email is None and self.phoneNumber is None:
            raise ValidationError("At least one of field1 or field2 must have a value.")

        def __str__(self):
            return f'{self.name} - {self.email}'

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    website_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.name}'


# Below are services, will be expanding as we add more and more of these services.

class RealEstateAgent(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    description = models.TextField()
    subCategory = ArrayField(models.CharField(max_length=200))
    regions = ArrayField(models.CharField(max_length=200))
    materialCost = JSONField()

class LaundryAppliances(models.Model):
    contractor = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    service = models.CharField(max_length=100)
    choice = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    #Cost of Material and Cost of Labour

    def __str__(self):
        return f'{self.contractor} - {self.service} - {self.choice}'

@receiver(pre_save, sender=LaundryAppliances)
def ensure_contractor_exists(sender, instance, **kwargs):
    # Check if the contractor already exists
    try:
        Contractor.objects.get(name=instance.contractor.name)
    except Contractor.DoesNotExist:
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