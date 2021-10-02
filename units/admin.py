from django.contrib import admin

from accounts.models import CustomUser
from .models import Task, Tip, Unit


# class Unit(admin.ModelAdmin):
#     fieldsets = [(None, {"fields": ["title"]})]


# Register your models here.
admin.site.register(Task)
admin.site.register(Tip)
admin.site.register(Unit)
