# Django
from django.shortcuts import render

# Rest framework
from rest_framework.generics import CreateAPIView

# local Django
from . serializer import UserCreationSerializer

# Create your views here.


class RegistrationView(CreateAPIView):
    serializer_class = UserCreationSerializer
