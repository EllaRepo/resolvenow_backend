from api.models import User, Complaint, Inspector
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'full_name', 'username', 'email', 'phone')

class InspectorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspector
        fields = ('id', 'full_name', 'username', 'email', 'phone', 'region', 'sector')

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        
        # These are claims, you can add custom claims
        token['full_name'] = user.full_name
        token['username'] = user.username
        token['email'] = user.email
        token['phone'] = user.phone
        token['image'] = str(user.profile.image)
        token['verified'] = user.profile.verified

        return token

class MyTokenObtainPairSerializer2(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, insp):
        token = super().get_token(insp)
        
        # These are claims, you can add custom claims
        token['full_name'] = insp.full_name
        token['email'] = insp.email
        token['phone'] = insp.phone
        token['region'] = insp.region
        token['sector'] = insp.sector

        return token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = ('full_name', 'email', 'username', 'phone', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            full_name=validated_data['full_name'],
            username=validated_data['username'],
            email=validated_data['email'],
            phone=validated_data['phone']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
    
class ComplaintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Complaint
        fields = ('email', 'username', 'compTitle', 'city', 'subCity', 'landmark', 'desc', 'region', 'compType', 'compSev')
    