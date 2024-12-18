from django.shortcuts import redirect, render
from django.template import TemplateDoesNotExist
from rest_framework import viewsets, status
from . import models
from . import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny


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


def activate(request,uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk = uid)
    except(User.DoesNotExist):
        user = None
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return redirect('login')
    else:
        return redirect('register')

class UserLoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = serializers.UserLoginSerializer(data=self.request.data)
        
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                token,_ = Token.objects.get_or_create(user=user)
                print(token)
                print(_)
                login(request, user)
                return Response({
                    'token': token.key,
                    'user_id': user.id
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'error': "Invalid username or password"
                }, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class UserLogoutView(APIView):
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get(self, request):
#         if hasattr(request.user, 'auth_token'):
#             request.user.auth_token.delete()
#         logout(request)
#         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

class UserLogoutView(APIView):
    def get(self, request):
        request.user.auth_token.delete()
        logout(request)
        return redirect('login')


