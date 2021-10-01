# api/serializers.py
from inspect import currentframe
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from pets.models import Pet, Breed, Streak, Journey


class SubBreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = ("name", "id")


class BreedSerializer(serializers.ModelSerializer):
    parent = SubBreedSerializer(read_only=True)

    class Meta:
        model = Breed
        fields = ("name", "img_url", "id", "parent")


class JourneySerializer(serializers.ModelSerializer):
    unit = serializers.IntegerField(default=1, initial=1)

    class Meta:
        model = Journey
        fields = ("id", "pet", "unit")


class PetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source="owner.id")
    journey = JourneySerializer(read_only=True)

    class Meta:
        model = Pet
        fields = ("id", "name", "owner", "breed", "age", "journey")


class StreakSerializer(serializers.ModelSerializer):
    class Meta:
        model = Streak
        fields = ("streakvalue", "pet")
