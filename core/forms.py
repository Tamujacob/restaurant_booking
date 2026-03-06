from django import forms
from .models import TableBooking

class TableBookingForm(forms.ModelForm):

    class Meta:
        model  = TableBooking
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'location',
            'date',
            'time',
            'guests',
            'special_requests',
        ]
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your first name',
                'id': 'bookFirst',
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Your last name',
                'id': 'bookLast',
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-input',
                'placeholder': 'you@email.com',
                'id': 'bookEmail',
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': '+256 700 000 000',
                'id': 'bookPhone',
            }),
            'location': forms.Select(attrs={
                'class': 'form-select',
                'id': 'bookLocation',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
                'id': 'bookDate',
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time',
                'id': 'bookTime',
            }),
            'guests': forms.Select(attrs={
                'class': 'form-select',
                'id': 'bookGuests',
            }),
            'special_requests': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Dietary requirements, birthday surprises, seating preferences…',
                'id': 'bookNote',
                'rows': 3,
            }),
        }