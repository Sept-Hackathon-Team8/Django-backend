from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Pet, Journey


@receiver(post_save, sender=Pet)
def create_pet_journey(sender, instance, created, **kwargs):
    if created:
        Journey.objects.create(pet=instance)
