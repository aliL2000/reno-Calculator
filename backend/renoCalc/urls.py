from django.urls import path, include
from rest_framework import routers
from renoCalc.views import user_choices_view
from renoCalc.views.contractor import ContractorViewSet
from renoCalc.views.user import UserViewSet
from renoCalc.views.user_auth_view import UserLoginView,UserStatusView

router = routers.DefaultRouter()
router.register(r"contractors", ContractorViewSet, basename="contractors")
router.register(r"users",UserViewSet, basename="users")

urlpatterns = [
    path("", include(router.urls)),
    path(
        "saveUserConfiguration/<int:userID>/",
        user_choices_view.saveUserConfiguration,
        name="saveUserConfiguration",
    ),
    path('login/', UserLoginView.as_view(), name='login'),
    path('user-status/', UserStatusView.as_view(), name='user-status'),
    # path("login/", views.login_user, name="login"),
    # path("logout", views.logout_user, name="logout"),
]
