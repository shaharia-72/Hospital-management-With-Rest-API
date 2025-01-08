# urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('doctor-specialization', views.DoctorSpecializationView, basename='doctor-specialization')
router.register('doctor-designation', views.DoctorDesignationView, basename='doctor-designation')
router.register('doctor-available-time', views.DoctorAvailableTimeView, basename='doctor-available-time')
router.register('doctor-list', views.DoctorView, basename='doctor-list')
router.register('doctor-detail', views.DoctorDetailView, basename='doctor-detail')
router.register('doctor-review', views.DoctorReviewView, basename='doctor-review')

urlpatterns = [
    path('', include(router.urls)),
]
