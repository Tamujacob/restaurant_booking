from django import forms
from .models import TableBooking, Order, CustomerFeedback
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StaffProfile


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

class OrderForm(forms.ModelForm):

    class Meta:
        model  = Order
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'delivery_location',
            'date',
            'delivery_time',
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
            'delivery_location': forms.TextInput(attrs={
                'class': 'form-input',
                'placeholder': 'Enter your delivery address',
                'id': 'orderLocation',
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-input',
                'type': 'date',
                'id': 'bookDate',
            }),
            'delivery_time': forms.TimeInput(attrs={
                'class': 'form-input',
                'type': 'time',
                'id': 'bookTime',
            }),
            
        } 

class CustomerFeedbackForm(forms.ModelForm):

    class Meta:
        model = CustomerFeedback
        fields = [
            'first_name',
            'last_name',
            'email',
            'phone',
            'branch_name',
            'rating',
            'message'
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
            'branch_name': forms.Select(attrs={
                'class': 'form-select',
                'id': 'branch',
            }),

            'rating': forms.RadioSelect(attrs={
                'class': 'star-rating',
            }),
              'message': forms.Textarea(attrs={
                'class': 'form-textarea',
                'placeholder': 'Write your message here.',
                'id': 'bookNote',
                'rows': 3,
            }),

        }   

class CustomerSignupForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name  = forms.CharField(max_length=100, required=True)
    email      = forms.EmailField(required=True)
 
    class Meta:
        model  = User
        fields = ['first_name', 
                  'last_name', 
                  'username',
                  'email', 
                  'password1', 
                  'password2'
                  ]          


class StaffCreationForm(UserCreationForm):
    email      = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=100, required=True)
    last_name  = forms.CharField(max_length=100, required=True)
    role       = forms.ChoiceField(choices=StaffProfile.ROLE_CHOICES)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'role']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_staff = True
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        if commit:
            user.save()
            StaffProfile.objects.create(user=user, role=self.cleaned_data['role'])
        return user        