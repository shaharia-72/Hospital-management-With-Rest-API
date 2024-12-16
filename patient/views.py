from django.shortcuts import render
from django.template import TemplateDoesNotExist
from rest_framework import viewsets, status
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


# Create your views here.

class PatientView(viewsets.ModelViewSet):
    queryset = models.Patient.objects.all()
    serializer_class = serializers.PatientSerializer

class UserRegistrationView(APIView):
    serializer_class = serializers.RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            # Save the user
            user = serializer.save()
            
            # Generate token and UID for activation link
            token = default_token_generator.make_token(user)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"


            email_subject = 'Activate Your Account'
            try:
                email_body = render_to_string('confirm_link.html', {'confirm_link': confirm_link})
            except TemplateDoesNotExist:
                 print("Template 'confirm_link.html' does not exist.")

            email = EmailMultiAlternatives(email_subject,'', to=[user.email])
            email.attach_alternative(email_body,"text/html")
            email.send()

            return Response(
                {'message': 'User registered successfully! A confirmation email has been sent.'},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
