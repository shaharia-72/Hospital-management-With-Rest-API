from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('DoctorSpecialization', views.DoctorSpecializationView)
router.register('DoctorDesignation', views.DoctorDesignationView)
router.register('DoctorAvailableTime', views.DoctorAvailableTimeView)
router.register('DoctorList', views.DoctorView)
router.register('DoctorReview', views.DoctorReviewView)


urlpatterns = [
    path('', include(router.urls)),
]