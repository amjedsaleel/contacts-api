# Django
from django.contrib.auth.models import User

# Rest framework work
from rest_framework import serializers


class UserCreationSerializer(serializers.ModelSerializer):
    """ Handles user creation serializer """
    first_name = serializers.CharField(max_length=50, allow_blank=False)
    email = serializers.EmailField(max_length=200, allow_blank=True)
    password = serializers.CharField(style={'input_type': 'password'}, max_length=255, write_only=True)
    password2 = serializers.CharField(style={'input_type': 'password'}, max_length=255, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'password2']

    def validate(self, attrs):
        """ Checks the passwords is matching or not """
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        """ Creates new user after all fields validated """
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user
