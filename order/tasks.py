from celery import shared_task
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from order.models import Order
from mt.settings import EMAIL_HOST_USER, DOMAIN


def _send_msg_to_email(order_instance: Order, template_name: str) -> None:
    subject = f'Замовлення #{order_instance.pk}'
    html_message = render_to_string(template_name, {'order': order_instance, "domain": DOMAIN})
    plain_message = strip_tags(html_message)
    from_email = EMAIL_HOST_USER
    to_email = order_instance.user_email
    send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)


@shared_task
def send_order_email(order_id: int) -> None:
    order = Order.objects.get(id=order_id)
    _send_msg_to_email(order, 'order_confirmation_email.html')


@shared_task
def check_determinate_of_orders() -> None:
    orders = Order.objects.filter(
        reminded=False,
        end_timestamp__gte=timezone.now().timestamp(),
        end_timestamp__lte=timezone.now().timestamp()+30*60
    )
    for order in orders:
        _send_msg_to_email(order, 'order_determinate.html')
        order.reminded = True
        order.save()
