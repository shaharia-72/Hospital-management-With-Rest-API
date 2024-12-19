from django.shortcuts import render
from rest_framework import viewsets,filters, pagination
from .import models
from .import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
# Create your views here.

class DoctorSpecializationView(viewsets.ModelViewSet):
    queryset = models.Specialization.objects.all()
    serializer_class = serializers.DoctorSpecializationSerializer

class DoctorDesignationView(viewsets.ModelViewSet):
    queryset = models.Designation.objects.all()
    serializer_class = serializers.DoctorDesignationSerializer

class AvailableTimeForSpecificDoctorView(filters.BaseFilterBackend):
    def filter_queryset(self,request,query_set, view):
        doctor_id = request.query_params.get('doctor_id')
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
        
class DoctorAvailableTimeView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = models.AvailableTime.objects.all()
    serializer_class = serializers.DoctorAvailableTimeSerializer
    filter_backends = [AvailableTimeForSpecificDoctorView]

class DoctorPaginationView(pagination.PageNumberPagination):
    page_size = 6  
    page_size_query_param = 'page_size'
    max_page_size = 100

class DoctorView(viewsets.ModelViewSet):
    queryset = models.Doctor.objects.all()
    serializer_class = serializers.DoctorSerializer
    filter_backends = [filters.SearchFilter]
    pagination_class = DoctorPaginationView
    search_fields = ['user__first_name', 'user__email', 'designation__name','specialization__name']

class DoctorReviewView(viewsets.ModelViewSet):
    queryset = models.Review.objects.all()
    serializer_class = serializers.DoctorReviewSerializer
    

