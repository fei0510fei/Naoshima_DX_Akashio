from rest_framework import serializers
from .models import DoData, WaterproofData

class DoDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoData
        fields = '__all__'

class WaterproofDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WaterproofData
        fields = '__all__'
