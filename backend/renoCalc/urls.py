from django.urls import path, include
from rest_framework import routers
from renoCalc import views
from renoCalc.views import ContractorViewSet

router = routers.DefaultRouter()
router.register(r"contractors", ContractorViewSet, basename="contractors")

urlpatterns = [
    path("", include(router.urls)),
    path("user/<int:userid>/saveUserchoices",views.my_view)
]
