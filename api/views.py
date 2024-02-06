import json
import logging
from datetime import datetime

from django.http import JsonResponse
from django.utils import timezone
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from twilio.rest import Client

from home.forms import MessageForm
from order.models import Order
from order.serializers import OrderSerializer
from mt.settings import TWILIO

logger = logging.getLogger("send-sms")


class SendSmsView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    @staticmethod
    def post(request):
        data = json.loads(request.body.decode("utf-8"))
        try:
            form = MessageForm(data)
            if form.is_valid():
                phone = data.get("phone")
                message = data.get("message")

                client = Client(TWILIO["sid"], TWILIO["token"])

                client.messages.create(from_=TWILIO["sender"], to=phone, body=message)

                logger.info(f"Message sended on {phone}. {datetime.now()}")
                return JsonResponse({"message": "SMS відправлено успішно"})

            return JsonResponse(
                {"error": "Помилка у номері чи повідомленні в запиті"}, status=400
            )

        except json.JSONDecodeError:
            return JsonResponse({"error": "Невірний формат JSON в запиті"}, status=400)

        except Exception as e:
            return JsonResponse(
                {"error": f"Помилка при відправці SMS: {str(e)}"}, status=500
            )


class OrderCreateView(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def create(self, request, *args, **kwargs):
        if request.data["end_timestamp"] > request.data[
            "start_timestamp"
        ] and request.data["end_timestamp"] > int(timezone.now().timestamp()):
            user_data = request.data.pop("user_data")
            request.data["user_email"] = user_data.get("email")
            request.data["user_name"] = user_data.get("name")
            return super().create(request, *args, **kwargs)
        return Response(
            {"error": "Invalid start_timestamp, end_timestamp params"},
            status=status.HTTP_400_BAD_REQUEST,
        )
