import json
from django.views.decorators.http import require_POST
from django.http import HttpResponse
from ..models import UserModel, UserHomeAndRenovationConfigurationModel

@require_POST
def saveUserConfiguration(request, userID):
    # Load JSON and UserID and save to the model
    homeAndRenoJSON = json.loads(request.body)
    userObject = UserModel.objects.get(pk=userID)
    UserConfigInstance = UserHomeAndRenovationConfigurationModel.objects.create(
        user=userObject, uniqueConfiguration=homeAndRenoJSON
    )
    UserConfigInstance.full_clean()
    UserConfigInstance.save()
    # TODO:Send an email to us with the JSON body
    return HttpResponse("This is a POST request.")