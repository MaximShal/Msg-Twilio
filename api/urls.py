from django.urls import path
from api.views import SendSmsView

urlpatterns = [
    path('send-sms/', SendSmsView.as_view(), name='api-send-sms'),
]
