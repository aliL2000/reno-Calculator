from django.urls import path, include
from rest_framework import routers
from renoCalc.views import user_choices_view
from renoCalc.views.contractor import ContractorViewSet

router = routers.DefaultRouter()
router.register(r"contractors", ContractorViewSet, basename="contractors")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "saveUserConfiguration/<int:userID>/",
        user_choices_view.saveUserConfiguration,
        name="saveUserConfiguration",
    ),
    # path("login/", views.login_user, name="login"),
    # path("logout", views.logout_user, name="logout"),
]
