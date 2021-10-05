# api/serializers.py
from inspect import currentframe
from django.db.models.query_utils import select_related_descend
from rest_framework import serializers
from pets.models import Pet, Breed, Streak, Journey, Assesment
from units.models import Unit, Task, Tip


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


class TipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tip
        fields = ("id", "title", "text", "success")


class TaskSerializer(serializers.ModelSerializer):
    tip = TipSerializer(many=True, read_only=True)

    class Meta:
        model = Task
        fields = ("id", "title", "instructions", "icon", "image", "order", "tip")


class UnitSerializer(serializers.ModelSerializer):
    tasks = TaskSerializer(many=True, read_only=True)

    class Meta:
        model = Unit
        fields = ("id", "title", "order", "tasks")


class AssesmentSerializer(serializers.ModelSerializer):
    task = serializers.IntegerField(source="task.order")
    unit = serializers.IntegerField(source="task.unit.order")

    class Meta:
        model = Assesment
        fields = ("success", "task", "unit")
