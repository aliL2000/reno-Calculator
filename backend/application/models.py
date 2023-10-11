from django.db import models
from django.core.exceptions import ValidationError
from django.dispatch import receiver
from django.db.models.signals import pre_save


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100, blank=True, null=True)
    phoneNumber = models.CharField(max_length=15, blank=True, null=True)
    address = models.CharField(max_length=100, blank=True, null=True)

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

#Below are services, will be expanding as we add more and more of these services.

class LaundryAppliances(models.Model):
    contractorName = models.ForeignKey(Contractor, on_delete=models.CASCADE)
    subService = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=10, decimal_places=2)

@receiver(pre_save, sender=LaundryAppliances)
def ensure_author_exists(sender, instance, **kwargs):
    # Check if the Author with the given name exists
    try:
        print(instance.contractorName.name)
        Contractor.objects.get(name=instance.contractorName.name)
    except Contractor.DoesNotExist:
        # Author does not exist, prevent saving the Book
        raise Exception("Contractor does not exist, ensure ")