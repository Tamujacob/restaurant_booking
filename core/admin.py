from django.contrib import admin
from .models import TableBooking

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'phone', 'location', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter   = ['status', 'location', 'date']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering      = ['-created_at']
    list_editable = ['status']