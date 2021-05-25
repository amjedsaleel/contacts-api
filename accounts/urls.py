# Django
from django.urls import path

# Rest framework
from rest_framework.routers import DefaultRouter

# local Django
from . import views

urlpatterns = [
    path('register/', views.RegistrationView.as_view())
]
