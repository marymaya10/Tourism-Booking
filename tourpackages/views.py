from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import TourPackage
from .serializers import TourPackageSerializer, TourPackageListSerializer


class TourPackageViewSet(viewsets.ModelViewSet):
    """ViewSet for TourPackage CRUD operations"""
    queryset = TourPackage.objects.all()
    serializer_class = TourPackageSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['destination', 'is_active', 'duration_days']
    search_fields = ['name', 'description', 'destination__name']
    ordering_fields = ['name', 'price', 'duration_days', 'created_at']
    ordering = ['-created_at']

    def get_queryset(self):
        """Filter out inactive packages unless explicitly requested"""
        queryset = super().get_queryset()
        if not self.request.query_params.get('include_inactive'):
            queryset = queryset.filter(is_active=True)
        return queryset

    def get_serializer_class(self):
        """Use list serializer for list action"""
        if self.action == 'list':
            return TourPackageListSerializer
        return TourPackageSerializer
