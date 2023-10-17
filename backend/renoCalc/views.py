from .models import Contractor
from .serializers import ContractorModelSerializer
from rest_framework import viewsets

class ContractorViewSet(viewsets.ModelViewSet):
    queryset = Contractor.objects.all()
    serializer_class = ContractorModelSerializer