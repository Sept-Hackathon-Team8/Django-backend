import uuid
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("journey", max_length=200)
    img_url = models.URLField("training photo", blank=True)
    progress = models.CharField("progress", max_length=200)

    def __str__(self):
        return self.name

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("task", max_length=200)
    description = models.CharField("description", max_length=200)
    journey = models.ManyToManyField(Journey, related_name="journey")
    img_url = models.URLField("task photo", blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name  