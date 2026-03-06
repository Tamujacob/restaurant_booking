from django.db import models

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
# Create your models here.
