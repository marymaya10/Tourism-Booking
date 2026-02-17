from rest_framework import viewsets, filters, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import Destination, Booking
from .serializers import DestinationSerializer, BookingSerializer


class DestinationViewSet(viewsets.ModelViewSet):
    """ViewSet for Destination CRUD operations"""
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['country', 'is_active', 'duration_days']
    search_fields = ['name', 'description', 'location', 'country']
    ordering_fields = ['name', 'price_per_person', 'rating', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter out inactive destinations unless explicitly requested"""
        queryset = super().get_queryset()
        if not self.request.query_params.get('include_inactive'):
            queryset = queryset.filter(is_active=True)
        return queryset


class BookingViewSet(viewsets.ModelViewSet):
    """ViewSet for Booking CRUD operations"""
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'booking_date', 'destination']
    search_fields = ['customer_name', 'customer_email', 'destination__name']
    ordering_fields = ['booking_date', 'created_at']
    ordering = ['-created_at']

    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        """Confirm a booking"""
        booking = self.get_object()
        if booking.status != 'pending':
            return Response(
                {'error': 'Only pending bookings can be confirmed'},
                status=status.HTTP_400_BAD_REQUEST
            )
        booking.status = 'confirmed'
        booking.save()
        return Response(BookingSerializer(booking).data)

    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Cancel a booking"""
        booking = self.get_object()
        if booking.status == 'cancelled':
            return Response(
                {'error': 'Booking is already cancelled'},
                status=status.HTTP_400_BAD_REQUEST
            )
        booking.status = 'cancelled'
        booking.save()
        return Response(BookingSerializer(booking).data)
