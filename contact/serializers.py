# Rest framework
from rest_framework.serializers import ModelSerializer

# local Django
from . models import Contact


class ContactSerializer(ModelSerializer):
    """
    Serialize Contacts
    """
    class Meta:
        model = Contact
        fields = ['id', 'user', 'first_name', 'last_name', 'picture', 'country_code', 'phone_number', 'is_favorite']
