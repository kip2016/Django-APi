from django.contrib import admin
from .models import Task
# Register your models here.
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
  list_display = ('id', 'title', 'description', 'created')
  fields = ('title', 'description')
  
  ordering = ('title', 'created', )