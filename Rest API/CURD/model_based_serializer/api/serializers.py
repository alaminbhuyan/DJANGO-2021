from rest_framework import serializers
from .models import Student

#* If we use ModelSerializer then we need not to assign create, update function manually 

class StudentSerializer(serializers.ModelSerializer):
    #* If we want to customize specific field properties
    #* read_only means I can only read the 'name' fields. I can't to write this fields
    name = serializers.CharField(read_only=True)
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
        # read_only_fields = ['name', 'roll'] #? this is another way
        # extra_kwargs = {'name':{'read_only':True}} #? this is also another way. we can use all field separate by comma.