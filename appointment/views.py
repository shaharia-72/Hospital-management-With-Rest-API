from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.
class AppointmentView(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        patient_id = self.request.query_params.get('patient_id')
        if patient_id:
            queryset = queryset.filter(patient__id=patient_id)  # Fixed filtering
        return queryset
            