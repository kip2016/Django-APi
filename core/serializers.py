from rest_framework import serializers
from .models import Task


#create your serializer here
class TaskSerializer(serializers.ModelSerializer):
  class Meta:
    model = Task
    fields = '__all__'