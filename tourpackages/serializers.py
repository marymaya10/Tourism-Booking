from rest_framework import serializers
from .models import TourPackage


class TourPackageSerializer(serializers.ModelSerializer):
    """Serializer for TourPackage model"""
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    
    class Meta:
        model = TourPackage
        fields = [
            'id', 'destination', 'destination_name', 'name', 'description',
            'price', 'duration_days', 'available_slots', 'is_active',
            'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class TourPackageListSerializer(serializers.ModelSerializer):
    """Serializer for TourPackage list view (minimal fields)"""
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    
    class Meta:
        model = TourPackage
        fields = [
            'id', 'destination', 'destination_name', 'name',
            'price', 'duration_days', 'available_slots', 'is_active'
        ]
