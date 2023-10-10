from django.db import models
from django.core.exceptions import ValidationError


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

    # # User must have EITHER email OR phoneNumber provided
    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             name="%(app_label)s_%(class)s_either_email_or_phoneNumber",
    #             check=(
    #                 models.Q(email__isnull=False) | models.Q(phoneNumber__isnull=False)
    #             ),
    #         )
    #     ]

    def clean(self):
        super().clean()
        if self.email is None and self.phoneNumber is None:
            raise ValidationError("At least one of field1 or field2 must have a value.")


class Contractor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    website_link = models.URLField(max_length=200, blank=True, null=True)
