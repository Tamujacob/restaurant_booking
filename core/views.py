from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm, OrderForm
from .models import MenuItem, Order, OrderItem
from django.http import JsonResponse
import json


def home(request):
    form = TableBookingForm()
    order_form = OrderForm()


    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f"Thank you, {booking.first_name}! Your table at Café Javas {booking.get_location_display()} is reserved for {booking.date} at {booking.time}.")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong. Please check your details and try again.")

    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'index.html', {
    'form': form,
    'order_form': order_form,    
    'menu_items': menu_items,
})

def admin_login(request):
    return render(request, 'login.html')

def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            # Step 3 — save order without committing to database yet
            order = form.save(commit=False)
            
            # Step 4 — get cart items sent from JavaScript
            cart_data = json.loads(request.POST.get('cart_items', '[]'))
            
            # Step 5 — calculate total price and save order
            total = sum(item['price'] * item['qty'] for item in cart_data)
            order.total_price = total
            order.save()
            
            # Step 6 — save each cart item as an OrderItem
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