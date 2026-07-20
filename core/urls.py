from django.urls import path
from . import views

urlpatterns = [

    # template routes
    path('', views.home, name='home'),
    path('login/', views.admin_login, name='login'),
    path('order/', views.place_order, name='place_order'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/toggle-user/<int:user_id>/', views.toggle_user, name='toggle_user'),

      #  Auth routes 
    path('signup/', views.customer_signup, name='customer_signup'),
    path('login/', views.customer_login, name='customer_login'),
    path('logout/', views.customer_logout, name='customer_logout'),
     path('staff-portal/', views.staff_login, name='staff_login'),


    # API routes
    path('api/menu/', views.api_menu, name='api_menu'),
    path('api/locations/', views.api_locations, name='api_locations'),
    path('api/bookings/', views.api_bookings, name='api_bookings'),
    path('api/orders/', views.api_orders, name='api_orders'),
    path('api/feedback/', views.api_feedback, name='api_feedback'),
]