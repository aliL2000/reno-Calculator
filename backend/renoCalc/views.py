import json
from .models import UserModel,ContractorModel,UserHomeAndRenovationConfigurationModel
from .serializers import ContractorModelSerializer
from rest_framework import viewsets
from django.views.decorators.http import require_POST
from django.http import HttpResponse

@require_POST
def saveUserConfiguration(request,userID):
    #Load JSON and UserID and save to the model
    homeAndRenoJSON = json.loads(request.body)
    userObject = UserModel.objects.get(pk=userID)
    UserConfigInstance = UserHomeAndRenovationConfigurationModel.objects.create(
        user = userObject,
        uniqueConfiguration = homeAndRenoJSON
    )
    UserConfigInstance.full_clean()
    UserConfigInstance.save()
    #TODO:Send an email to us with the JSON body
    return HttpResponse("This is a POST request.")

# @require_http_methods(["GET", "POST"])
# def my_view(request):
#     # I can assume now that only GET or POST requests make it this far
#     # ...
#     pass


class ContractorViewSet(viewsets.ModelViewSet):
    queryset = ContractorModel.objects.all()
    serializer_class = ContractorModelSerializer
