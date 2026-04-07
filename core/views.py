from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm, OrderForm, CustomerFeedbackForm
from .models import MenuItem, Order, OrderItem, Location, CustomerFeedback
from django.http import JsonResponse
import json


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
        
           

    