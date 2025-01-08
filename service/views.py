from rest_framework import viewsets
from rest_framework.mixins import RetrieveModelMixin
from . import models, serializers

class ServiceView(viewsets.ModelViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer

class ServiceDetailView(RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = models.Service.objects.all()
    serializer_class = serializers.ServiceSerializer
