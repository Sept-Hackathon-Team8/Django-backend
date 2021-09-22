# api/serializers.py
from rest_framework import serializers
from pets.models import Breed


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ("name", "img_url", "id", "parent")
