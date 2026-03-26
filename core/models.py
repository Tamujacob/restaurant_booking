from django.db import models
# Create your models here.

class TableBooking(models.Model):

    # LOCATION CHOICES 
    LOCATION_CHOICES = [
        ('kira_road', 'Kira Road'),
        ('kampala_boulevard', 'Kampala Boulevard'),
        ('oasis_mall', 'Oasis Mall'),
        ('nakawa', 'Nakawa'),
        ('namirembe', 'Namirembe'),
        ('lugogo', 'Lugogo'),
        ('bombo_road', 'Bombo Road'),
        ('parliamentary_avenue', 'Parliamentary Avenue'),
        ('victoria_mall_entebbe', 'Victoria Mall, Entebbe'),
    ]

    #  GUEST CHOICES 
    GUEST_CHOICES = [
        (1, '1 Person'),
        (2, '2 People'),
        (3, '3 People'),
        (4, '4 People'),
        (5, '5 People'),
        (6, '6 People'),
        (10, '7 – 10 People'),
        (11, '11+ People (Group)'),
    ]

    #  STATUS CHOICES 
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('confirmed', 'Confirmed'),
        ('cancelled', 'Cancelled'),
        ('completed', 'Completed'),
    ]

    #  CUSTOMER DETAILS 
    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    email         = models.EmailField()
    phone         = models.CharField(max_length=20, blank=True)

    #  BOOKING DETAILS 
    location      = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    date          = models.DateField()
    time          = models.TimeField()
    guests        = models.IntegerField(choices=GUEST_CHOICES, default=2)
    special_requests = models.TextField(blank=True)

    # STATUS & TIMESTAMPS ─
    status        = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at    = models.DateTimeField(auto_now_add=True)
    updated_at    = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']       # newest bookings first
        verbose_name = 'Table Booking'
        verbose_name_plural = 'Table Bookings'

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.location} on {self.date} at {self.time}"

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class MenuItem(models.Model):

    #categories
    CATEGORY_CHOICES = [
    ('breakfast', 'Breakfast'),
    ('mains', 'Mains'),
    ('drinks', 'Drinks'),
    ('desserts', 'Desserts'),
]
    cat = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    name = models.CharField(max_length=50)
    desc = models.TextField()
    price = models.IntegerField()
    badge = models.CharField(max_length=50, blank=True)
    emoji = models.CharField(max_length=10)
    img = models.URLField()
    is_available = models.BooleanField(default=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name
         
class Order(models.Model): 

    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('approved', 'Approved'),
        ('out_for_delivery', 'Out for Delivery'),
        ('delivered', 'Delivered'),
        ('cancelled', 'Cancelled'),
    ]


    #  CUSTOMER DETAILS 
    first_name        = models.CharField(max_length=100)
    last_name         = models.CharField(max_length=100)
    email             = models.EmailField()
    phone             = models.CharField(max_length=20, blank=True)
    delivery_location = models.CharField(max_length=100)
    date              = models.DateField()
    total_price       = models.IntegerField()
    status            = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    delivery_time     = models.TimeField()
    created_at        = models.DateTimeField(auto_now_add=True)
    updated_at        = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Order'
        verbose_name_plural = 'Orders'

    def __str__(self):
        return f"{self.first_name} {self.last_name} — {self.date} at {self.delivery_time}"
    
class OrderItem(models.Model) :

    #order_details
    item_name        = models.CharField( max_length=150)    
    order            = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item        = models.ForeignKey(MenuItem, on_delete=models.SET_NULL, null=True)
    quantity         = models.IntegerField()
    unit_price       = models.IntegerField()    
    
    class Meta:
        verbose_name = 'Order Item'
        verbose_name_plural = 'Order Items'
    
    def __str__(self):
        return f"{self.item_name} x{self.quantity} at UGX {self.unit_price}"
    
    @property
    def total_price(self):
        return self.unit_price * self.quantity   


class Location(models.Model):
    branch_name     = models.CharField(max_length=150)
    address         = models.CharField(max_length=150)
    city            = models.CharField(max_length=150)
    phone           = models.CharField(max_length=20, blank=True)
    opening_time    = models.TimeField()
    closing_time    = models.TimeField()
    is_active       = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'location'
        verbose_name_plural = 'locations'
    
    def __str__(self):
        return self.branch_name

class customerFeedback(models.Model):

    LOCATION_CHOICES = [
        ('kira_road', 'Kira Road'),
        ('kampala_boulevard', 'Kampala Boulevard'),
        ('oasis_mall', 'Oasis Mall'),
        ('nakawa', 'Nakawa'),
        ('namirembe', 'Namirembe'),
        ('lugogo', 'Lugogo'),
        ('bombo_road', 'Bombo Road'),
        ('parliamentary_avenue', 'Parliamentary Avenue'),
        ('victoria_mall_entebbe', 'Victoria Mall, Entebbe'),
    ]

    RATING_CHOICES = [
        (1, '1 - Very Poor'),
        (2, '2 - Poor'),
        (3, '3 - Average'),
        (4, '4 - Good'),
        (5, '5 - Excellent'),
    ]

    first_name    = models.CharField(max_length=100)
    last_name     = models.CharField(max_length=100)
    email         = models.EmailField()
    phone         = models.CharField(max_length=50, blank=True)
    date          = models.DateField()
    branch_name   = models.CharField(max_length=50, choices=LOCATION_CHOICES)
    message       = models.TextField()
