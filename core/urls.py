from django.urls import path
from . import views

urlpatterns = [
    path('api/menu/', views.api_menu, name='api_menu'),
    path('api/locations/', views.api_locations, name='api_locations'),
    path('api/bookings/', views.api_bookings, name='api_bookings'),
    path('api/orders/', views.api_orders, name='api_orders'),
    path('api/feedback/', views.api_feedback, name='api_feedback'),
]