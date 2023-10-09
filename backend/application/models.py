from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)

    #User must have EITHER email OR phoneNumber provided
    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_either_email_or_phoneNumber",
                check=(
                    models.Q(email__isnull=False) | models.Q(phoneNumber__isnull=False)
                ),
            )
        ]

class Contractor(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=15)
    address = models.CharField(max_length=100)
    website_link = models.URLField(max_length=200, blank=True, null=True)