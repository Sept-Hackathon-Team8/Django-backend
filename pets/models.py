import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import CustomUser

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
    breed = models.ForeignKey(Breed, related_name="streak", on_delete=CASCADE)

    def __str__(self):
        return self.name


class Streak(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    streakvalue = models.IntegerField("streak count", default=0)
    pet = models.OneToOneField(Pet, related_name="streak", on_delete=CASCADE)

    def __str__(self):
        return f"{self.pet.name} streak: {self.streakvalue}"
