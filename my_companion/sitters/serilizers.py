from rest_framework import serializers
from .models import Sitter

class SitterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sitter
        fields = ['id', 'name', 'phone_number', 'email', 'zip_code', 'rate']