from rest_framework import serializers
from .models import contact_data

class ContactSerializer(serializers.ModelSerializer):

    class Meta:
        model = contact_data
        fields = ('id', 'name', 'email', 'phone', 'enquiry', 'enquiry_date')

