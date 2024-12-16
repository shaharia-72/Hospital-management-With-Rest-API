from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .import views

router = DefaultRouter()

router.register('List', views.PatientView)


urlpatterns = [
    path('', include(router.urls)),
]