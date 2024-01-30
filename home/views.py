import logging
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from twilio.rest import Client

from home.forms import MessageForm
from mt.settings import TWILIO

logger = logging.getLogger("send-sms")


class HomeView(View):
    template_name = "send_sms.html"

    def get(self, request):
        return render(request, self.template_name, {"form": MessageForm()})


class SendSmsView(View):
    template_name = "send_sms.html"

    def post(self, request):
        form = MessageForm(request.POST)

        if form.is_valid():
            phone = form.cleaned_data["phone"]
            message = form.cleaned_data["message"]

            client = Client(TWILIO["sid"], TWILIO["token"])
            message = client.messages.create(
                from_=TWILIO["sender"], to=phone, body=message
            )

            logger.info(f"Message sended on {phone}. {datetime.now()}")
            return HttpResponse(f"Повідомлення відправлено на номер {phone}: {message}")

        else:
            return render(request, self.template_name, {"form": form})
