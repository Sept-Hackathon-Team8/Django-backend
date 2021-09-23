from .models import CustomUser
from rest_framework import serializers
from dj_rest_auth.models import TokenModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["url", "username", "email", "groups"]


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TokenModel
        fields = ("key", "user")
