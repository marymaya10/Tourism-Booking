from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator

from destinations.models import Destination


class TourPackage(models.Model):
    """Model representing a tour package that can be booked"""
    
    destination = models.ForeignKey(
        Destination, 
        on_delete=models.CASCADE, 
        related_name='packages'
    )
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    duration_days = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    available_slots = models.PositiveIntegerField(
        default=0,
        validators=[MinValueValidator(0)]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} - {self.destination.name}"
