# Django
from django.urls import path

# local Django
from . import views

urlpatterns = [
    path('', views.Contact.as_view(), name='contact')
]