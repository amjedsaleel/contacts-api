# Django
from django.urls import path

# local Django
from . import views

urlpatterns = [
    path('', views.Contacts.as_view(), name='contact'),
    path('<int:pk>/', views.ContactDetail.as_view(), name='contact-detail')
]
