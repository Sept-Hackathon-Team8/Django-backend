import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import CustomUser
from datetime import datetime, timedelta

from units.models import Task


# Create your models here.


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("breed", max_length=200)
    parent = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    img_url = models.URLField("dog photo", blank=True)

    def __str__(self):
        return self.name


class Pet(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    owner = models.ForeignKey(CustomUser, related_name="pets", on_delete=CASCADE)
    breed = models.ForeignKey(Breed, related_name="breeds", on_delete=CASCADE)

    def __str__(self):
        return self.name


class Streak(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    streak_value = models.IntegerField(default=0)
    pet = models.ForeignKey(Pet, related_name="streak", on_delete=CASCADE)

    class Meta:
        ordering = ["-created_at"]

    def is_streak(self):
        now = datetime.now(self.updated_at.tzinfo)
        hours_to_end_of_day = timedelta(hours=25 - now.hour)
        day_delta = timedelta(days=1)
        return now < self.updated_at + day_delta + hours_to_end_of_day

    def calc_streak(self):
        if self.is_streak():
            self.streak_value = (
                datetime.now(self.created_at.tzinfo) - self.created_at
            ).days

    def __str__(self):
        return f"{self.pet.name} - streak: {self.streak_value}"


class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    pet = models.OneToOneField(Pet, related_name="journey", on_delete=CASCADE)
    unit = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.pet} journey"


class Assesment(models.Model):
    # SORT BY DATE IN THE VIEW SERIALIZER
    created_at = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    success = models.BooleanField(default=False)
    task = models.ForeignKey(Task, related_name="task", on_delete=CASCADE)
    pet = models.ForeignKey(Pet, related_name="pet", on_delete=CASCADE)

    def __str__(self):
        type = "great" if self.success else "ruff"
        return f"Assesment - Unit: {self.task.unit.order} - {self.task.title} - {type}"
