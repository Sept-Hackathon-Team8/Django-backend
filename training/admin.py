from django.contrib import admin
from .models import Journey
from .models import Unit
from .models import Task
from .models import TaskAssessment
# Register your models here.
admin.site.register(Journey)
admin.site.register(Unit)
admin.site.register(Task)
admin.site.register(TaskAssessment)