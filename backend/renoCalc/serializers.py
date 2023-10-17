from django.core import serializers
from .models import Contractor
from rest_framework import serializers


class ContractorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contractor
        fields = ("name", "email", "phoneNumber", "address", "website", "rating")
