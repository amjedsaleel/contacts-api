# Django
from django.urls import path

# Rest framework
from rest_framework import authtoken

# local Django
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view()),
    path('api-token-auth/', views.CustomAuthToken.as_view())
]
