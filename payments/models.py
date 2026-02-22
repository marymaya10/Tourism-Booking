from django.db import models
from django.core.validators import MinValueValidator

from destinations.models import Booking


class Payment(models.Model):
    """Model representing a payment for a booking"""
    
    PAYMENT_METHODS = [
        ('mpesa', 'M-Pesa'),
        ('card', 'Credit/Debit Card'),
        ('bank', 'Bank Transfer'),
        ('cash', 'Cash'),
    ]
    
    PAYMENT_STATUS = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    )
    
    booking = models.OneToOneField(
        Booking, 
        on_delete=models.CASCADE, 
        related_name='payment'
    )
    amount = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        validators=[MinValueValidator(0)]
    )
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHODS)
    payment_status = models.CharField(
        max_length=20, 
        choices=PAYMENT_STATUS, 
        default='pending'
    )
    transaction_reference = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f"Payment for Booking {self.booking.pk} - {self.payment_status}"
    
    def save(self, *args, **kwargs):
        """Auto confirm booking when payment is completed"""
        if self.booking and self.payment_status == 'completed' and self.booking.status == 'pending':
            self.booking.status = 'confirmed'
            self.booking.save()
            
            # Reduce available slots
            package = self.booking.package
            if package and package.available_slots is not None:
                package.available_slots -= self.booking.number_of_guests
                if package.available_slots < 0:
                    package.available_slots = 0
                package.save()
        
        super().save(*args, **kwargs)
