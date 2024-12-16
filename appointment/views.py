from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.
class AppointmentView(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class = serializers.AppointmentSerializer