from rest_framework import serializers
from .models import CallRecord

class CallRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CallRecord
        fields = '__all__'
