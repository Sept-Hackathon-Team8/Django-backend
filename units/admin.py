from django.contrib import admin
from .models import Task, Tip, Unit

# Register your models here.
admin.site.register(Task)
admin.site.register(Tip)
admin.site.register(Unit)
