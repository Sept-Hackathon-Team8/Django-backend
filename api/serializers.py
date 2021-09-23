# api/serializers.py
from rest_framework import serializers
from pets.models import Breed


class SubBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ("name", "id")


class BreedSerializer(serializers.ModelSerializer):
    parent = SubBreedSerializer(read_only=True)

    class Meta:
        model = Breed
        fields = ("name", "img_url", "id", "parent")
