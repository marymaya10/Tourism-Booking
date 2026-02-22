from rest_framework import serializers
from .models import Payment


class PaymentSerializer(serializers.ModelSerializer):
    """Serializer for Payment model"""
    booking_reference = serializers.IntegerField(source='booking.id', read_only=True)
    
    class Meta:
        model = Payment
        fields = [
            'id', 'booking', 'booking_reference', 'amount', 
            'payment_method', 'payment_status', 'transaction_reference',
            'phone_number', 'created_at', 'updated_at'
        ]
        read_only_fields = ['id', 'payment_status', 'created_at', 'updated_at']


class PaymentCreateSerializer(serializers.ModelSerializer):
    """Serializer for creating Payment"""
    
    class Meta:
        model = Payment
        fields = [
            'booking', 'amount', 'payment_method', 'transaction_reference', 'phone_number'
        ]
    
    def create(self, validated_data):
        """Override to trigger auto-confirm logic"""
        return super().create(validated_data)


class PaymentStatusUpdateSerializer(serializers.ModelSerializer):
    """Serializer for updating payment status (e.g., from M-Pesa callback)"""
    
    class Meta:
        model = Payment
        fields = ['payment_status', 'transaction_reference']
