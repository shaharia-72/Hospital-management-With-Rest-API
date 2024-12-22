from rest_framework import serializers
from . import models

class AppointmentSerializer(serializers.ModelSerializer):
    time = serializers.PrimaryKeyRelatedField(queryset=models.AvailableTime.objects.all())
    patient = serializers.PrimaryKeyRelatedField(queryset=models.Patient.objects.all())
    doctor = serializers.PrimaryKeyRelatedField(queryset=models.Doctor.objects.all())

    class Meta:
        model = models.Appointment
        fields = '__all__'
