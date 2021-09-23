from django.contrib import admin
from .models import Breed, Streak, Pet, Journey, Assesment


from .models import Streak

# Register your models here.
admin.site.register(Breed)
admin.site.register(Streak)
admin.site.register(Pet)
admin.site.register(Journey)
admin.site.register(Assesment)
