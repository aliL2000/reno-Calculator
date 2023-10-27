from rest_framework import serializers
from ..models import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = ('id', 'email', 'phoneNumber', 'address', 'first_name', 'last_name')