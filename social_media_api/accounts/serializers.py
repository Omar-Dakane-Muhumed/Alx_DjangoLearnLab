from rest_framework import serializers
from rest_framework.authtoken.models import Token
from .models import CustomUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers']

lf, data):
        """
        Ensure the passwords match during validation.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """
        Use create_user method to ensure the password is hashed.
        """
        validated_data.pop('confirm_password')  # Remove confirm_password before creating the user
        return User.objects.create_user(**validated_data)


from rest_framework import serializers
from django.contrib.auth import get_user_model

# Get the custom user model
User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    # Explicitly declare password fields
    password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})
    confirm_password = serializers.CharField(write_only=True, min_length=8, style={'input_type': 'password'})

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'bio', 'profile_picture', 'followers', 'password', 'confirm_password']
        extra_kwargs = {
            'email': {'required': True},
        }

    def validate(self, data):
        """
        Ensure the passwords match during validation.
        """
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """
        Use create_user method to ensure the password is hashed.
        """
        validated_data.pop('confirm_password')  # Remove confirm_password before creating the user
        return User.objects.create_user(**validated_data)
