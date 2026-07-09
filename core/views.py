from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm, OrderForm, CustomerFeedbackForm
from .models import MenuItem, Order, OrderItem, Location, CustomerFeedback
from django.http import JsonResponse
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import (
    MenuItemSerializer, LocationSerializer,
    OrderSerializer, FeedbackSerializer, TableBookingSerializer,
)
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    form = TableBookingForm()
    order_form = OrderForm()
    feedback_form = CustomerFeedbackForm()


    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f"Thank you, {booking.first_name}! Your table at Café Javas {booking.get_location_display()} is reserved for {booking.date} at {booking.time}.")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong. Please check your details and try again.")

    menu_items = MenuItem.objects.filter(is_available=True)
    locations = Location.objects.filter(is_active = True)
    return render(request, 'index.html', {
    'form': form,
    'order_form': order_form,    
    'menu_items': menu_items,
    'locations':locations,
    'feedback_form': feedback_form
})

def admin_login(request):
    return render(request, 'login.html')

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
           
            cart_data = json.loads(request.POST.get('cart_items', '[]'))
            
            total = sum(item['price'] * item['qty'] for item in cart_data)
            order.total_price = total
            order.save()
           
            for item in cart_data:
                menu_item = MenuItem.objects.get(id=item['id'])
                OrderItem.objects.create(
                    order      = order,
                    menu_item  = menu_item,
                    item_name  = item['name'],
                    quantity   = item['qty'],
                    unit_price = item['price'],
                )

           
            return JsonResponse({'status': 'success', 'message': f"Thank you {order.first_name}! Your order has been placed and will be delivered to {order.delivery_location}."})
            
        else:
            return JsonResponse({'status': 'error', 'message': 'Please fill in all required fields correctly.'})
    
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})

def submit_feedback(request):
    if request.method == 'POST':
        form = CustomerFeedbackForm(request.POST)
        if form.is_valid():
            feedback = form.save() 
            messages.success(request, f"Thank you {feedback.first_name}! Your feedback has been received.")
            return redirect('home')  

        else:
                messages.error(request, "Something went wrong. Please try again.")
        return redirect('home')     
        
           

    # --- API VIEWS ---

@api_view(['GET'])
def api_menu(request):
    items = MenuItem.objects.filter(is_available=True)
    serializer = MenuItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def api_locations(request):
    locations = Location.objects.filter(is_active=True)
    serializer = LocationSerializer(locations, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def api_bookings(request):
    serializer = TableBookingSerializer(data=request.data)
    if serializer.is_valid():
        booking = serializer.save()
        return Response(
            {'message': f"Table booked for {booking.first_name}!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_orders(request):
    serializer = OrderSerializer(data=request.data)
    if serializer.is_valid():
        order = serializer.save()
        return Response(
            {'message': f"Order placed for {order.first_name}!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def api_feedback(request):
    serializer = FeedbackSerializer(data=request.data)
    if serializer.is_valid():
        feedback = serializer.save()
        return Response(
            {'message': f"Feedback received from {feedback.first_name}!"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@staff_member_required
def dashboard(request):
    bookings = TableBooking.objects.all().order_by('-created_at')
    orders = Order.objects.all().order_by('-created_at')
    feedbacks = CustomerFeedback.objects.all().order_by('-created_at')

    context = {
        'total_bookings': bookings.count(),
        'total_orders': orders.count(),
        'total_feedback': feedbacks.count(),
        'bookings': bookings,
        'orders': orders,
        'feedbacks': feedbacks,
    }
    return render(request, 'dashboard.html', context)