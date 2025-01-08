from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# Register the Service viewset with a specific basename
router.register('services', views.ServiceView, basename='service')
router.register('service-detail', views.ServiceDetailView, basename='service-detail')

urlpatterns = [
    path('', include(router.urls)),
]
