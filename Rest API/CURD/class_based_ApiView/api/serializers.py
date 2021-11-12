from rest_framework import serializers
from .models import Student

# If we use ModelSerializer then we need not to assign create, update function manually 

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','name', 'roll', 'city']