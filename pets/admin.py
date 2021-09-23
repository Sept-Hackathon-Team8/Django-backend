from django.contrib import admin
from .models import Breed, Streak, Pet
from .models import Streak

# Register your models here.
admin.site.register(Breed)
admin.site.register(Streak)
admin.site.register(Pet)
