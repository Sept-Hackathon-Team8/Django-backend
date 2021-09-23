# api/serializers.py
from rest_framework import serializers
from pets.models import Pet, Breed, Streak


class SubBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ("name", "id")


class BreedSerializer(serializers.ModelSerializer):
    parent = SubBreedSerializer(read_only=True)

    class Meta:
        model = Breed
        fields = ("name", "img_url", "id", "parent")


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")

    class Meta:
        model = Pet
        fields = ("id", "name", "owner", "breed")


class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = ("streakvalue", "pet")
