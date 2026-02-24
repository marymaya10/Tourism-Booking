from rest_framework import serializers
from .models import Destination, Booking, Review


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
        
        # Check available slots (overbooking prevention)
        if package.available_slots is not None and number_of_guests > package.available_slots:
            raise serializers.ValidationError(
                f"Not enough available slots. Only {package.available_slots} slots available."
            )
        
        validated_data['total_price'] = package.price * number_of_guests
        return super().create(validated_data)


class ReviewSerializer(serializers.ModelSerializer):
    """Serializer for Review model"""
    user_username = serializers.CharField(source='user.username', read_only=True)
    destination_name = serializers.CharField(source='destination.name', read_only=True)
    
    class Meta:
        model = Review
        fields = [
            'id', 'user', 'user_username', 'destination', 'destination_name',
            'rating', 'comment', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'user', 'created_at', 'updated_at']
