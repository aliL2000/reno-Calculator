from .models import ContractorModel
from .serializers import ContractorModelSerializer
from rest_framework import viewsets
from django.views.decorators.http import require_POST
from django.http import HttpResponse

@require_POST
def my_view(request,userID):

    
    return HttpResponse("This is a POST request.")

# @require_http_methods(["GET", "POST"])
# def my_view(request):
#     # I can assume now that only GET or POST requests make it this far
#     # ...
#     pass


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = ContractorModel.objects.all()
    serializer_class = ContractorModelSerializer
