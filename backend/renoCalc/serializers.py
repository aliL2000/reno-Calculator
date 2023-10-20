from django.core import serializers
from .models import ContractorModel
from rest_framework import serializers


class ContractorModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractorModel
        fields = ("name", "email", "phoneNumber", "address", "website", "rating")
