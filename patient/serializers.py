# from rest_framework import serializers
# from .import models
# from django.contrib.auth.models import User

# class PatientSerializer(serializers.ModelSerializer):
#     user  = serializers.StringRelatedField(many=False)
#     class Meta:
#         model = models.Patient
#         fields = '__all__'

# class RegistrationSerializer(serializers.ModelSerializer):
#     confirm_password = serializers.CharField(required=True)
#     phone_no = serializers.CharField(required=True, max_length=12,allow_blank=True)
#     image = serializers.ImageField(required=True,allow_null=True)
#     # class Meta:
#     #     model = User
#     #     fields = ['username', 'first_name', 'last_name','email','password','confirm_password']
#     #     extra_kwargs = {
#     #         'password': {'write_only': True}
#     #     }
#     class Meta:
#             model = User
#             fields = ['username', 'first_name', 'last_name','email','password','confirm_password', 'phone_no', 'image']
#             extra_kwargs = {
#                 'password': {'write_only': True}
#             }

#     def validate(self, data):
#         if data['password'] != data['confirm_password']:
#             raise serializers.ValidationError({'password': 'Passwords not match. Try again'})

#         if User.objects.filter(email=data['email']).exists():
#             raise serializers.ValidationError({'email': 'Email already exists.'})
#         return data

#     def save(self):
#         user = User(
#             username=self.validated_data['username'],
#             email=self.validated_data['email'],
#             first_name=self.validated_data['first_name'],
#             last_name=self.validated_data['last_name']
#         )
#         user.set_password(self.validated_data['password'])
#         user.is_active = False
#         user.save()

#         patient = models.Patient(
#             user=user,
#             phone_no=self.validated_data['phone_no'],
#             image=self.validated_data['image']
#         )
#         patient.save()
#         return user
    
# class UserLoginSerializer(serializers.Serializer):
#     username = serializers.CharField(required=True)
#     password = serializers.CharField(required=True)

from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Patient
        fields = '__all__'


class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    phone_no = serializers.CharField(required=True, max_length=12)
    image = serializers.ImageField(required=True, allow_null=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'phone_no', 'image']
        extra_kwargs = {'password': {'write_only': True, 'style': {'input_type': 'password'}}}

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords do not match.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'A user with this email already exists.'})
        return data

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(self.validated_data['password'])
        user.is_active = False  # Requires activation
        user.save()

        Patient.objects.create(
            user=user,
            phone_no=self.validated_data['phone_no'],
            image=self.validated_data['image']
        )
        return user


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True, style={'input_type': 'password'})
