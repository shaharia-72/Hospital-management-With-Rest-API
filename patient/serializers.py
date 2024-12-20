from rest_framework import serializers
from .import models
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user  = serializers.StringRelatedField(many=False)
    class Meta:
        model = models.Patient
        fields = '__all__'

    def get_full_name(self, obj):
        if obj.user:
            return f"{obj.user.first_name} {obj.user.last_name}"
        return None

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name','email','password','confirm_password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError({'password': 'Passwords not match. Try again'})

        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Email already exists.'})
        return data

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name']
        )
        user.set_password(self.validated_data['password'])
        user.is_active = False
        user.save()
        return user
    
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)