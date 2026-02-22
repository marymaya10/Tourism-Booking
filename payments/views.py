from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Payment
from .serializers import PaymentSerializer, PaymentCreateSerializer, PaymentStatusUpdateSerializer


class PaymentViewSet(viewsets.ModelViewSet):
    """ViewSet for Payment CRUD operations"""
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['payment_status', 'payment_method', 'booking']
    search_fields = ['transaction_reference', 'booking__customer_name']
    ordering_fields = ['created_at', 'amount']
    ordering = ['-created_at']
    
    def get_serializer_class(self):
        if self.action == 'create':
            return PaymentCreateSerializer
        if self.action in ['update_status', 'partial_update']:
            return PaymentStatusUpdateSerializer
        return PaymentSerializer
    
    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        """Update payment status - used for payment gateway callbacks"""
        payment = self.get_object()
        new_status = request.data.get('payment_status')
        transaction_ref = request.data.get('transaction_reference')
        
        if new_status not in ['pending', 'completed', 'failed', 'refunded']:
            return Response(
                {'error': 'Invalid payment status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        payment.payment_status = new_status
        if transaction_ref:
            payment.transaction_reference = transaction_ref
        payment.save()
        
        return Response(PaymentSerializer(payment).data)
    
    @action(detail=False, methods=['get'], url_path='by-booking/(?P<booking_id>[^/.]+)')
    def by_booking(self, request, booking_id=None):
        """Get payment for a specific booking"""
        try:
            payment = Payment.objects.get(booking_id=booking_id)
            return Response(PaymentSerializer(payment).data)
        except Payment.DoesNotExist:
            return Response(
                {'error': 'Payment not found for this booking'},
                status=status.HTTP_404_NOT_FOUND
            )
