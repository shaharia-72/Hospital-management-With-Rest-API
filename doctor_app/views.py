from django.shortcuts import render
from rest_framework import viewsets
from .import models
from .import serializers
# Create your views here.

class DoctorSpecializationView(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.DoctorSpecializationSerializer

class DoctorDesignationView(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DoctorDesignationSerializer

class DoctorAvailableTimeView(viewsets.ModelViewSet):
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.DoctorAvailableTimeSerializer

class DoctorView(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer

class DoctorReviewView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.DoctorReviewSerializer
