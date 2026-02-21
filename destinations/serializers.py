from rest_framework import serializers
from .models import Destination, Booking


class DestinationSerializer(serializers.ModelSerializer):
    """Serializer for Destination model"""
    
    class Meta:
        model = Destination
        fields = [
            'id', 'name', 'description', 'location', 'country',
            'image_url', 'price_per_person', 'duration_days',
            'rating', 'is_active', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class BookingSerializer(serializers.ModelSerializer):
    """Serializer for Booking model"""
    package_name = serializers.CharField(source='package.name', read_only=True)
    destination_name = serializers.CharField(source='package.destination.name', read_only=True)
    
    class Meta:
        model = Booking
        fields = [
            'id', 'package', 'package_name', 'destination_name', 'customer_name',
            'customer_email', 'number_of_guests', 'booking_date',
            'status', 'total_price', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'status', 'created_at', 'updated_at']
    
    def create(self, validated_data):
        """Calculate total price based on package price and number of guests"""
        package = validated_data['package']
        number_of_guests = validated_data['number_of_guests']
        validated_data['total_price'] = package.price * number_of_guests
        return super().create(validated_data)
