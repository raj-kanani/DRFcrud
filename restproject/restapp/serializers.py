from rest_framework import serializers
from .models import Student


#  using model-serializer with CRUD
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Student
#         fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    name = serializers.CharField(read_only=True)  # single field readonly cannot update

    class Meta:
        model = Student
        fields = '__all__'
        # read_only_fields = ['name', 'city']  # multiple field only readonly cannot change
        extra_kwargs = {'name': {'read_only': True}}  # single field readonly cannot change


# # Simple serializer with CRUD
# # validators
# def start_with_r(value):
#     if value[0].lower() != 'r':  # check 0 index
#         raise serializers.ValidationError('name start with R')
#
#
# class StudentSerializer(serializers.Serializer):
#     name = serializers.CharField(max_length=100, validators=[start_with_r])
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
#
#     def create(self, validate_data):
#         return Student.objects.create(**validate_data)
#
#     def update(self, instance, validated_data):
#         print(instance.name)
#         instance.name = validated_data.get('name', instance.name)
#         print(instance.name)
#         instance.roll = validated_data.get('roll', instance.roll)
#         instance.city = validated_data.get('city', instance.city)
#         instance.save()
#         return instance
#
#     # field level validation
#     def validate_roll(self, value):
#         if value >= 200:
#             raise serializers.ValidationError("Seat Full")
#         return value
#
#     # object level validation
#     def validate(self, data):  # data get all fields
#         nm = data.get('name')
#         ct = data.get('city')
#         if nm.lower() == 'raj' and ct.lower() != 'rajkot':
#             raise serializers.ValidationError('city is Rajkot')
#         return data
