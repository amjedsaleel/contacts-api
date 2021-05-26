# Django
from django.shortcuts import render

# Rest framework
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from  rest_framework import status

# local Django
from . models import Contact
from . serializers import ContactSerializer

# Create your views here.


class Contacts(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ContactDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = ContactSerializer

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'Status': 'Contact is deleted'}, status=status.HTTP_204_NO_CONTENT)
