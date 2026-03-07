from django.contrib import admin
from .models import TableBooking, MenuItem

@admin.register(TableBooking)
class TableBookingAdmin(admin.ModelAdmin):
    list_display  = ['full_name', 'email', 'phone', 'location', 'date', 'time', 'guests', 'status', 'created_at']
    list_filter   = ['status', 'location', 'date']
    search_fields = ['first_name', 'last_name', 'email', 'phone']
    ordering      = ['-created_at']
    list_editable = ['status']

@admin.register(MenuItem)
class MenuItemAdmin(admin.ModelAdmin):
    list_display = ['cat', 'name', 'price', 'badge', 'is_available']
    list_filter = ['cat', 'is_available']
    search_fields = ['name', 'cat']
    list_editable = ['is_available']