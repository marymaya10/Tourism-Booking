from django.contrib import admin
from .models import TourPackage


@admin.register(TourPackage)
class TourPackageAdmin(admin.ModelAdmin):
    list_display = ['name', 'destination', 'price', 'duration_days', 'available_slots', 'is_active']
    list_filter = ['destination', 'is_active', 'duration_days']
    search_fields = ['name', 'description', 'destination__name']
    list_editable = ['is_active']
