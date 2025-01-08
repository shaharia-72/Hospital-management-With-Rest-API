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


# # Create your views here.

# class PatientView(viewsets.ModelViewSet):
#     queryset = models.Patient.objects.all()
#     serializer_class = serializers.PatientSerializer

# class UserRegistrationView(APIView):
#     serializer_class = serializers.RegistrationSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)

#         if serializer.is_valid():
#             # Save the user
#             user = serializer.save()
#             # patient = models.Patient.objects.get(user=user)

#             patient = models.Patient.objects.create(
#                 user=user,
#                 phone_no=serializer.validated_data['phone_no'],
#                 image=serializer.validated_data['image']
#             )
            
#             # Generate token and UID for activation link
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             confirm_link = f"http://127.0.0.1:8000/patient/active/{uid}/{token}"


#             email_subject = 'Activate Your Account'
#             try:
#                 email_body = render_to_string('confirm_link.html', {'confirm_link': confirm_link})
#             # except TemplateDoesNotExist:
#             #      print("Template 'confirm_link.html' does not exist.")

#                 email = EmailMultiAlternatives(email_subject,'', to=[user.email])
#                 email.attach_alternative(email_body,"text/html")
#                 email.send()
#             except Exception as e:
#                 user.delete()  # Rollback user creation
#                 return Response(
#                     {'error': "Failed to send activation email. Please try again later."},
#                     status=status.HTTP_500_INTERNAL_SERVER_ERROR
#                 )

#             return Response(
#                 {'message': 'User registered successfully! A confirmation email has been sent.',
#                 'user_id': user.id,
#                 'patient_id': patient.id
#                 },
#                 status=status.HTTP_201_CREATED
#             )
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def activate(request,uid64, token):
#     try:
#         uid = urlsafe_base64_decode(uid64).decode()
#         user = User._default_manager.get(pk = uid)
#     except (User.DoesNotExist, ValueError, TypeError):
#         user = None
    
#     if user is not None and default_token_generator.check_token(user, token):
#         user.is_active = True
#         user.save()
#         return redirect('login.html')
#     else:
#         return redirect('register')

# class UserLoginView(APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         serializer = serializers.UserLoginSerializer(data=self.request.data)
        
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']

#             user = authenticate(username=username, password=password)

#             if user:
#                 token,_ = Token.objects.get_or_create(user=user)
#                 patient = models.Patient.objects.get(user=user)
#                 # print(token)
#                 # print(_)
#                 login(request, user)
#                 return Response({
#                     'token': token.key,
#                     'user_id': user.id,
#                     'patient_id': patient.id
#                 }, status=status.HTTP_200_OK)
#             else:
#                 return Response({
#                     'error': "Invalid username or password"
#                 }, status=status.HTTP_401_UNAUTHORIZED)
        
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# # class UserLogoutView(APIView):
# #     authentication_classes = [TokenAuthentication]
# #     permission_classes = [IsAuthenticated]

# #     def get(self, request):
# #         if hasattr(request.user, 'auth_token'):
# #             request.user.auth_token.delete()
# #         logout(request)
# #         return Response({'message': 'Successfully logged out'}, status=status.HTTP_200_OK)

# class UserLogoutView(APIView):
#     def get(self, request):
#         request.user.auth_token.delete()
#         logout(request)
#         return redirect('login')


from django.shortcuts import redirect
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer
from django.shortcuts import redirect, render
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import authenticate, login, logout
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from .models import Patient
from .serializers import PatientSerializer, RegistrationSerializer, UserLoginSerializer


### View for Managing Patients
class PatientView(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


### View for User Registration
# class UserRegistrationView(APIView):
#     serializer_class = RegistrationSerializer

#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # Save user and create patient
#             user = serializer.save()
#             Patient.objects.create(
#                 user=user,
#                 phone_no=serializer.validated_data['phone_no'],
#                 image=serializer.validated_data['image']
#             )

#             # Generate activation link
#             token = default_token_generator.make_token(user)
#             uid = urlsafe_base64_encode(force_bytes(user.pk))
#             activation_link = f"{request.scheme}://{request.get_host()}/patient/activate/{uid}/{token}"

#             # Send activation email
#             email_subject = 'Activate Your Account'
#             email_body = render_to_string('confirm_link.html', {'confirm_link': activation_link})
#             email = EmailMultiAlternatives(email_subject, email_body, to=[user.email])
#             email.attach_alternative(email_body, "text/html")

#             try:
#                 email.send()
#             except Exception as e:
#                 user.delete()  # Rollback user creation
#                 return Response({'error': 'Failed to send activation email. Please try again.'},
#                                 status=status.HTTP_500_INTERNAL_SERVER_ERROR)

#             return Response({'message': 'Registration successful! Check your email to activate your account.'},
#                             status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.db import IntegrityError

class UserRegistrationView(APIView):
    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            try:
                # Save the user
                user = serializer.save()

                # Check if the user already has a Patient record
                if Patient.objects.filter(user=user).exists():
                    return Response({'error': 'A patient record already exists for this user.'},
                                    status=status.HTTP_400_BAD_REQUEST)

                # Create the Patient record
                Patient.objects.create(
                    user=user,
                    phone_no=serializer.validated_data['phone_no'],
                    image=serializer.validated_data.get('image', None)
                )

                # Generate activation link
                token = default_token_generator.make_token(user)
                uid = urlsafe_base64_encode(force_bytes(user.pk))
                activation_link = f"{request.scheme}://{request.get_host()}/patient/activate/{uid}/{token}"

                # Send activation email
                email_subject = 'Activate Your Account'
                email_body = render_to_string('confirm_link.html', {'confirm_link': activation_link})
                email = EmailMultiAlternatives(email_subject, email_body, to=[user.email])
                email.attach_alternative(email_body, "text/html")

                email.send()

                return Response({'message': 'Registration successful! Check your email to activate your account.'},
                                status=status.HTTP_201_CREATED)

            except IntegrityError:
                # Handle unique constraint violation gracefully
                user.delete()  # Rollback user creation
                return Response({'error': 'A user with this information already exists.'},
                                status=status.HTTP_400_BAD_REQUEST)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


### Account Activation View
def activate(request, uid64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uid64))
        user = User.objects.get(pk=uid)
    except (User.DoesNotExist, ValueError, TypeError):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        # Redirect to login page
        return redirect('/patient/login/')
    # Redirect to registration page if activation fails
    return redirect('/patient/register/')


### Login View
# class UserLoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = UserLoginSerializer(data=request.data)
#         if serializer.is_valid():
#             username = serializer.validated_data['username']
#             password = serializer.validated_data['password']
#             user = authenticate(username=username, password=password)

#             if user:
#                 if not user.is_active:
#                     return Response({'error': 'Account is not activated. Please check your email.'},
#                                     status=status.HTTP_401_UNAUTHORIZED)

#                 token, _ = Token.objects.get_or_create(user=user)
#                 login(request, user)
#                 return Response({'token': token.key, 'user_id': user.id, 'username': user.username},
#                                 status=status.HTTP_200_OK)

#             return Response({'error': 'Invalid username or password.'}, status=status.HTTP_401_UNAUTHORIZED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Validate the serializer data
        serializer = serializers.UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            # Authenticate the user
            user = authenticate(username=username, password=password)

            # Check if the user exists
            if user:
                # Check if the account is active
                if not user.is_active:
                    return Response({
                        'error': 'Account is not activated. Please check your email for activation.'
                    }, status=status.HTTP_401_UNAUTHORIZED)

                # Ensure token exists or create one
                token, created = Token.objects.get_or_create(user=user)

                # Check if the user has a corresponding patient record
                try:
                    patient = models.Patient.objects.get(user=user)
                except models.Patient.DoesNotExist:
                    return Response({
                        'error': 'Patient record not found. Please contact support.'
                    }, status=status.HTTP_404_NOT_FOUND)

                # Log the user in
                login(request, user)

                # Respond with the token and relevant user info
                return Response({
                    'token': token.key,
                    'user_id': user.id,
                    'patient_id': patient.id,
                    'username': user.username
                }, status=status.HTTP_200_OK)

            # Invalid username or password
            return Response({
                'error': 'Invalid username or password.'
            }, status=status.HTTP_401_UNAUTHORIZED)

        # If serializer is not valid, return errors
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

### Logout View
class UserLogoutView(APIView):
    def get(self, request):
        if hasattr(request.user, 'auth_token'):
            request.user.auth_token.delete()
        logout(request)
        return Response({'message': 'Logged out successfully.'}, status=status.HTTP_200_OK)
