from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api/manage/menu', views.MenuItemViewSet, basename='menuitem')

urlpatterns = [

    # template routes
    path('', views.home, name='home'),
    path('order/', views.place_order, name='place_order'),
    path('feedback/', views.submit_feedback, name='submit_feedback'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/toggle-user/<int:user_id>/', views.toggle_user, name='toggle_user'),
    path('dashboard/order-status/<int:order_id>/', views.update_order_status, name='update_order_status'),

    #  Auth routes
    path('signup/', views.customer_signup, name='customer_signup'),
    path('login/', views.customer_login, name='customer_login'),
    path('logout/', views.customer_logout, name='customer_logout'),
    path('staff-portal/', views.staff_login, name='staff_login'),
    path('dashboard/create-staff/', views.create_staff, name='create_staff'),
    path('physical-order/', views.physical_order, name='physical_order'),

    # API routes
    path('api/menu/', views.api_menu, name='api_menu'),
    path('api/locations/', views.api_locations, name='api_locations'),
    path('api/bookings/', views.api_bookings, name='api_bookings'),
    path('api/orders/', views.api_orders, name='api_orders'),
    path('api/feedback/', views.api_feedback, name='api_feedback'),

    path('accounts/', include('allauth.urls')),
]

urlpatterns += router.urls

urlpatterns += router.urls