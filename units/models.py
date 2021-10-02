import uuid
from django.db import models
from django.db.models.deletion import CASCADE
from accounts.models import CustomUser
from datetime import datetime, timedelta


class Unit(models.Model):
    # class Meta:
    #     ordering = ["order", "task.order"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    order = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Task(models.Model):
    class Meta:
        ordering = ["unit__order", "order"]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    instructions = models.TextField(max_length=1000)
    icon_url = models.URLField("task icon", blank=True)
    img_url = models.URLField("task image", blank=True)
    order = models.IntegerField(default=0)
    unit = models.ForeignKey(Unit, related_name="task", on_delete=CASCADE)

    def __str__(self):
        return f"{self.unit} task: {self.title}"


class Tip(models.Model):
    success = models.BooleanField(default=False)
    title = models.CharField(max_length=200)
    text = models.TextField(max_length=1000)
    task = models.ForeignKey(Task, related_name="tip", on_delete=CASCADE)

    def __str__(self):
        type = "great" if self.success else "ruff"
        return f"Unit: {self.task.unit.order} - {self.task.title} - {type}"
