from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm, OrderForm
from .models import MenuItem, Order, OrderItem



def home(request):
    form = TableBookingForm()

    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save()
            messages.success(request, f"Thank you, {booking.first_name}! Your table at Café Javas {booking.get_location_display()} is reserved for {booking.date} at {booking.time}.")
            return redirect('home')
        else:
            messages.error(request, "Something went wrong. Please check your details and try again.")

    menu_items = MenuItem.objects.filter(is_available=True)
    return render(request, 'index.html', {'form': form, 'menu_items': menu_items})


def admin_login(request):
    return render(request, 'login.html')