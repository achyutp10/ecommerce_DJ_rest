from django.shortcuts import render
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated

from userauths.models import User, Profile
from userauths.serializers import MyTokenObtainPairSerializer, ProfileSerializer, RegisterSerializer, UserSerializer
import random
# from shortuuid.django_fields import ShortUUIDField
import shortuuid
from rest_framework_simplejwt.tokens import RefreshToken
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status


class MyTokenObtainPairView(TokenObtainPairView):
  serializer_class = MyTokenObtainPairSerializer
  
class RegisterView(generics.CreateAPIView):
  queryset = User.objects.all()
  permission_classes = [AllowAny]
  serializer_class = RegisterSerializer

def generate_otp():
  uuid_key = shortuuid.uuid()
  unique_key = uuid_key[:6]
  return unique_key

def generate_numeric_otp(length=7):
        # Generate a random 7-digit OTP
        otp = ''.join([str(random.randint(0, 9)) for _ in range(length)])
        return otp

class PasswordResetEmailVerify(generics.RetrieveAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer
    
    def get_object(self):
        email = self.kwargs['email']
        user = User.objects.get(email=email)
        
        if user:
            user.otp = generate_numeric_otp()
            uidb64 = user.pk
             
             # Generate a token and include it in the reset link sent via email
            refresh = RefreshToken.for_user(user)
            reset_token = str(refresh.access_token)

            # Store the reset_token in the user model for later verification
            user.reset_token = reset_token
            user.save()

            link = f"http://localhost:5173/create-new-password?otp={user.otp}&uidb64={uidb64}&reset_token={reset_token}"
            
            merge_data = {
                'link': link, 
                'username': user.username, 
            }
            subject = f"Password Reset Request"
            text_body = render_to_string("email/password_reset.txt", merge_data)
            html_body = render_to_string("email/password_reset.html", merge_data)
            
            msg = EmailMultiAlternatives(
                subject=subject, from_email=settings.FROM_EMAIL,
                to=[user.email], body=text_body
            )
            msg.attach_alternative(html_body, "text/html")
            msg.send()
        return user

class PasswordChangeView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        payload = request.data
        otp = payload['otp']
        uidb64 = payload['uidb64']  
        password = payload['password']

        user = User.objects.get(id=uidb64, otp=otp)
        if user:
            user.set_password(password)
            user.reset_token=""
            user.save()

            return Response({"detail": "Password changed successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "Invalid OTP or User"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
  

class ProfileAPIView(generics.RetrieveUpdateAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [AllowAny]

    def get_object(self): 
        user_id = self.kwargs['user_id']

        user = User.objects.get(id=user_id)
        profile = Profile.objects.get(user=user)
        return profile
  