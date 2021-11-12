from rest_framework import serializers, validators
from .models import Student


# Validators
def starts_with_r(value):
    if value[0].lower() != 'a':
        raise serializers.ValidationError("Name should start with 'A' ")

# If we use ModelSerializer then we need not to assign create, update function manually.
class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(validators=[starts_with_r])
    class Meta:
        model = Student
        fields = ['name', 'roll', 'city']
    # Adding validators 
    # Field level validators for 'roll' field
    def validate_roll(self, value):
        if value >= 1050:
            raise serializers.ValidationError("Seat full")
        return value
    
    # Object level validation
    def validate(self, data):
        name = data.get('name')
        city = data.get('city')
        if name.lower() == "alamin" and city.lower() != 'comilla':
            raise serializers.ValidationError("City must be Comilla")
        return data