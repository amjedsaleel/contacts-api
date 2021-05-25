# Django
from django.shortcuts import render

# Rest framework
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

# local Django
from . models import Contact
from . serializers import ContactSerializer

# Create your views here.


class Contacts(ListCreateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
