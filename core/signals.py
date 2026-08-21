from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.conf import settings
from .models import Order, TableBooking


# ── ORDER STATUS EMAILS ──────────────────────────

@receiver(pre_save, sender=Order)
def track_old_order_status(sender, instance, **kwargs):
    """Stash the previous status on the instance before it's saved."""
    if instance.pk:
        try:
            instance._old_status = Order.objects.get(pk=instance.pk).status
        except Order.DoesNotExist:
            instance._old_status = None
    else:
        instance._old_status = None


@receiver(post_save, sender=Order)
def send_order_status_email(sender, instance, created, **kwargs):
    if created:
        return  # don't email on initial creation, only on status changes

    old_status = getattr(instance, '_old_status', None)
    if old_status == instance.status:
        return  # status didn't actually change

    if not instance.email:
        return  # physical orders may not have an email

    status_messages = {
        'approved': "Your order has been approved and is being prepared.",
        'out_for_delivery': "Your order is out for delivery!",
        'delivered': "Your order has been delivered. Enjoy your meal!",
        'cancelled': "Your order has been cancelled.",
    }
    message = status_messages.get(instance.status)
    if not message:
        return

    send_mail(
        subject=f"Harvest & Hearth — Order Update (#{instance.id})",
        message=f"Hi {instance.first_name},\n\n{message}\n\nThank you for choosing Harvest & Hearth.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
        fail_silently=True,
    )


# ── BOOKING STATUS EMAILS ────────────────────────

@receiver(pre_save, sender=TableBooking)
def track_old_booking_status(sender, instance, **kwargs):
    if instance.pk:
        try:
            instance._old_status = TableBooking.objects.get(pk=instance.pk).status
        except TableBooking.DoesNotExist:
            instance._old_status = None
    else:
        instance._old_status = None


@receiver(post_save, sender=TableBooking)
def send_booking_status_email(sender, instance, created, **kwargs):
    if created:
        return

    old_status = getattr(instance, '_old_status', None)
    if old_status == instance.status:
        return

    status_messages = {
        'confirmed': f"Your table at {instance.get_location_display()} is confirmed for {instance.date} at {instance.time}.",
        'cancelled': "Your table booking has been cancelled.",
        'completed': "Thanks for dining with us! We hope you enjoyed your visit.",
    }
    message = status_messages.get(instance.status)
    if not message:
        return

    send_mail(
        subject=f"Harvest & Hearth — Booking Update",
        message=f"Hi {instance.first_name},\n\n{message}\n\nThank you for choosing Harvest & Hearth.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=[instance.email],
        fail_silently=True,
    )