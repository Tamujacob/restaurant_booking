from django.contrib import admin
from .models import TableBooking, MenuItem, Order, OrderItem, Location

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
    
@admin.register(Order)  
class OrderAdmin(admin.ModelAdmin):
    list_display    = [ 'first_name', 'last_name', 'email', 'phone', 'delivery_location', 'date', 'total_price', 'status', 'created_at']  
    list_filter     = [ 'status', 'date', 'delivery_location']
    search_fields   = [ 'first_name', 'last_name', 'email', 'phone']
    ordering        = ['-created_at']
    list_editable   = ['status', 'date', 'delivery_location']

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display   = [ 'item_name', 'order', 'menu_item', 'quantity', 'unit_price'] 
    list_filter    = [ 'item_name', 'menu_item'] 
    search_fields  = ['item_name']
    list_editable  = ['quantity']
    
@admin.register(Location)    
class LocationAdmin(admin.ModelAdmin):
    list_display  = ['branch_name', 'address', 'city', 'phone', 'opening_time', 'closing_time', 'is_active']
    list_filter   = ['branch_name', 'address', 'city']
    search_fields = ['branch_name']
    list_editable = ['opening_time', 'closing_time', 'is_active']
