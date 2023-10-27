from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

UserModel = get_user_model()

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None):
        try:
            user = UserModel.objects.get(email=email)
            if user.check_password(password) and user.is_active:
                return user
        except UserModel.DoesNotExist:
            pass
        return None