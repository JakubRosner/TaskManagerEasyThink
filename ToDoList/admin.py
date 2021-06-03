from django.contrib import admin
from .models import Task
# Registered Task model
# User model is already integrated
admin.site.register(Task)
