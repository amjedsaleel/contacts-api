# Rest framework
from rest_framework import serializers

# local Django
from . models import Contact


class ContactSerializer(serializers.ModelSerializer):
    """
    Serialize Contacts
    """
    user = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = Contact
        fields = ['id', 'user', 'first_name', 'last_name', 'picture', 'country_code', 'phone_number', 'is_favorite']
