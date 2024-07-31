from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from userauths.models import User, Profile
from django.contrib.auth.password_validation import validate_password


# Login serialiazer
class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
  @classmethod
  def get_token(cls, user):
    token = super().get_token(user)

    token['full_name'] = user.full_name
    token['email'] = user.email
    token['username'] = user.username
    try:
      token['vendor_id'] = user.vendor.id
    except:
      token['vendor_id'] = 0
      
    return token

class RegisterSerializer(serializers.ModelSerializer):
  password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
  password2 = serializers.CharField(write_only=True, required=True)
  class Meta:
    model = User
    fields = ['full_name', 'email', 'phone', 'password', 'password2']
  
  def validate(self, attrs):
    if attrs['password'] != attrs['password2']:
      raise serializers.ValidationError({"password" :"Passwords does not match"})
    return attrs
  
  def create(self, validated_data):
    user = User.objects.create(
      full_name=validated_data['full_name'],
      email=validated_data['email'],
      phone=validated_data['phone'],
    )
    email_user, _ = user.email.split("@")
    user.username = email_user
    user.set_password(validated_data['password'])
    user.save()

    return user

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = "__all__"

class ProfileSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Profile
    fields = "__all__"
  
  def to_representation(self, instance):
    response = super().to_representation(instance)
    response['user'] = UserSerializer(instance.user).data
    return response

