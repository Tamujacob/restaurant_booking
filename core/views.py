from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm, OrderForm, CustomerFeedbackForm, CustomerSignupForm 
from .models import MenuItem, Order, OrderItem, Location, CustomerFeedback, TableBooking
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
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from functools import wraps
from django.core.exceptions import PermissionDenied
from django.utils import timezone
from .models import StaffProfile, MenuItem, Order, OrderItem
from .forms import StaffCreationForm



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
        else:
            messages.error(request, "Something went wrong. Please try again.")
        return redirect('home')

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

# ── Customer Signup ──────────────────────────────────────────
def customer_signup(request):
    form = CustomerSignupForm()
 
    if request.method == 'POST':
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, f"Welcome, {user.first_name}! Your account has been created.")
            return redirect('home')
        else:
            messages.error(request, "Please fix the errors below and try again.")
 
    return render(request, 'customer_signup.html', {'form': form})
 
 
# ── Customer Login ───────────────────────────────────────────
def customer_login(request):
    if request.user.is_authenticated:
        return redirect('home')

    next_url = request.GET.get('next') or request.POST.get('next') or 'home'

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            if user.is_staff:
                # staff trying to log in via customer page — redirect them
                messages.error(request, "Staff members should use the staff portal.")
                return redirect('customer_login')
            login(request, user)
            messages.success(request, f"Welcome back, {user.first_name}!")
            return redirect(next_url)
        else:
            messages.error(request, "Invalid username or password. Please try again.")

    return render(request, 'customer_login.html', {'next': next_url})
 
# ── Customer Logout ──────────────────────────────────────────
def customer_logout(request):
    logout(request)
    messages.success(request, "You have been signed out.")
    return redirect('home')
 
 
# ── Staff Login ──────────────────────────────────────────────
def staff_login(request):
    if request.user.is_authenticated and request.user.is_staff:
        return redirect('dashboard')
 
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
 
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('dashboard')
        elif user is not None and not user.is_staff:
            # valid user but not staff
            messages.error(request, "You do not have staff access.")
        else:
            messages.error(request, "Invalid credentials. Please try again.")
 
    return render(request, 'staff_login.html')


@staff_member_required
def dashboard(request):
    bookings  = TableBooking.objects.all().order_by('-created_at')
    orders    = Order.objects.all().order_by('-created_at')
    feedbacks = CustomerFeedback.objects.all().order_by('-created_at')
    users     = User.objects.filter(is_staff=False).order_by('-date_joined')  # customers only

    context = {
        'total_bookings': bookings.count(),
        'total_orders':   orders.count(),
        'total_feedback': feedbacks.count(),
        'total_users':    users.count(),
        'bookings':       bookings,
        'orders':         orders,
        'feedbacks':      feedbacks,
        'users':          users,
    }
    return render(request, 'dashboard.html', context)

@staff_member_required
def toggle_user(request, user_id):
    if request.method == 'POST':
        user = get_object_or_404(User, id=user_id, is_staff=False)
        user.is_active = not user.is_active
        user.save()
        status = "activated" if user.is_active else "deactivated"
        messages.success(request, f"{user.username} has been {status}.")
    return redirect('dashboard')

def staff_role_required(*allowed_roles):
    """Superusers and Managers get full access. Other roles must be in allowed_roles."""
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped(request, *args, **kwargs):
            if not request.user.is_authenticated or not request.user.is_staff:
                messages.error(request, "You must be logged in as staff to access this page.")
                return redirect('staff_login')
            if request.user.is_superuser:
                return view_func(request, *args, **kwargs)
            profile = getattr(request.user, 'staff_profile', None)
            if profile and (profile.role == 'manager' or profile.role in allowed_roles):
                return view_func(request, *args, **kwargs)
            raise PermissionDenied
        return _wrapped
    return decorator


@login_required
def create_staff(request):
    if not request.user.is_superuser:
        raise PermissionDenied

    if request.method == 'POST':
        form = StaffCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, f"Staff account created for {user.get_full_name() or user.username}.")
            return redirect('create_staff')
    else:
        form = StaffCreationForm()

    staff_list = StaffProfile.objects.select_related('user').all()
    return render(request, 'create_staff.html', {'form': form, 'staff_list': staff_list})


@staff_role_required('receptionist_physical')
def physical_order(request):
    menu_items = MenuItem.objects.filter(is_available=True)

    if request.method == 'POST':
        customer_name = request.POST.get('customer_name', '').strip()
        table_number = request.POST.get('table_number', '').strip()

        order_items = []
        total_price = 0
        for item in menu_items:
            qty = request.POST.get(f'qty_{item.id}')
            if qty and qty.isdigit() and int(qty) > 0:
                qty = int(qty)
                order_items.append((item, qty))
                total_price += item.price * qty

        if not order_items:
            messages.error(request, "Select at least one item before submitting.")
        else:
            name_parts = customer_name.split(' ', 1) if customer_name else ['Walk-in', 'Customer']
            first_name = name_parts[0]
            last_name = name_parts[1] if len(name_parts) > 1 else ''

            order = Order.objects.create(
                first_name=first_name,
                last_name=last_name,
                date=timezone.now().date(),
                delivery_time=timezone.now().time(),
                total_price=total_price,
                status='approved',
                source='physical',
                table_number=table_number,
                handled_by=request.user,
            )
            for item, qty in order_items:
                OrderItem.objects.create(
                    order=order,
                    menu_item=item,
                    item_name=item.name,
                    quantity=qty,
                    unit_price=item.price,
                )
            messages.success(request, f"Order #{order.id} placed — table {table_number or 'walk-in'} — UGX {total_price}.")
            return redirect('physical_order')

    return render(request, 'physical_order.html', {'menu_items': menu_items})
 