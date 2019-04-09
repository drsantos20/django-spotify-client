from rest_framework import serializers
from ..models import User


class UserSerializer(serializers.ModelSerializer):

    email = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ['email']
