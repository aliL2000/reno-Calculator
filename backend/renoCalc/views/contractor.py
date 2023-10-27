import json
from ..models import UserModel, ContractorModel, UserHomeAndRenovationConfigurationModel
from ..serializers.contractor_serializer import ContractorModelSerializer
from rest_framework import viewsets

class ContractorViewSet(viewsets.ModelViewSet):
    queryset = ContractorModel.objects.all()
    serializer_class = ContractorModelSerializer
