# Django
from django.shortcuts import render

# Rest framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.


class Contact(APIView):
    def get(self, request):
        return Response("OK")

