from decimal import Decimal

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User


class Destination(models.Model):
    """Model representing a tourism destination"""
    name = models.CharField(max_length=200)
    description = models.TextField()
    location = models.CharField(max_length=200)
    country = models.CharField(max_length=100)
    image_url = models.URLField(blank=True, null=True)
    price_per_person = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    duration_days = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    rating = models.DecimalField(
        max_digits=2, 
        decimal_places=1,
        default=Decimal('0.0'),
        validators=[MinValueValidator(Decimal('0')), MaxValueValidator(Decimal('5'))]
    )
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.name


class Booking(models.Model):
    """Model representing a booking"""
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
    ]
    
    # Link to TourPackage instead of directly to Destination
    # (TourPackage already links to Destination)
    package = models.ForeignKey(
        'tourpackages.TourPackage', 
        on_delete=models.CASCADE,
        related_name='bookings',
        null=True,
        blank=True
    )
    customer_name = models.CharField(max_length=200)
    customer_email = models.EmailField()
    number_of_guests = models.PositiveIntegerField(
        validators=[MinValueValidator(1)]
    )
    booking_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending'
    )
    total_price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.customer_name} - {self.package.name}"


class Review(models.Model):
    """Model representing a review for a destination"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE, related_name='reviews')
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ('user', 'destination')

    def __str__(self):
        return f"{self.user.username} - {self.destination.name} - {self.rating}/5"
