from django.db.models.signals import post_save
from django.dispatch import receiver
from order.models import Order
from order.tasks import send_order_email


@receiver(post_save, sender=Order)
def send_order_confirmation_email(sender, instance, created, **kwargs):
    if created:
        send_order_email.delay(instance.id)
