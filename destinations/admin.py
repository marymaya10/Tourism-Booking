from django.contrib import admin
from .models import Destination, Booking


@admin.register(Destination)
class DestinationAdmin(admin.ModelAdmin):
    list_display = ['name', 'country', 'price_per_person', 'duration_days', 'rating', 'is_active']
    list_filter = ['country', 'is_active', 'duration_days']
    search_fields = ['name', 'description', 'location', 'country']
    list_editable = ['is_active']


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'package', 'booking_date', 'number_of_guests', 'status', 'total_price']
    list_filter = ['status', 'booking_date', 'package']
    search_fields = ['customer_name', 'customer_email', 'package__name']
    list_editable = ['status']
