import uuid
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.

class Journey(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("journey", max_length=200)
    img_url = models.URLField("training photo", blank=True)
    unit = models.ManyToManyField(Unit, related_name="unit")

    def __str__(self):
        return self.name


class Unit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("unit", max_length=200)
    task = models.OneToOneField(Task, related_name="task")
    journey = models.ManyToManyField(Journey, related_name="journey")
    status = models.BooleanField(default=False)
    progress = models.CharField("progress", max_length=200)

    def __str__(self):
        return self.name  

class Task(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("task", max_length=200)
    instructions = models.CharField("instructions", max_length=200)
    unit = models.OneToOneField(Unit, related_name="unit")
    img_url = models.URLField("task photo", blank=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name  

class TaskAssessment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("taskassessment", max_length=200)
    task = models.ManyToManyField(Task, related_name="task")
    img_url = models.URLField("taskassessment photo", blank=True)
    progress = models.CharField("progress", max_length=200)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name 