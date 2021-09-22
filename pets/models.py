import uuid
from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Pet(models.Model):
    pass


class Breed(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField("breed", max_length=200)
    parent = models.ForeignKey("self", on_delete=CASCADE, blank=True, null=True)
    img_url = models.URLField("dog photo", blank=True)

    def __str__(self):
        return self.name
