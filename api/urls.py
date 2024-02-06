from django.urls import path

from api.views import SendSmsView, OrderCreateView

urlpatterns = [
    path("send-sms/", SendSmsView.as_view(), name="api-send-sms"),
    path(
        "orders/", OrderCreateView.as_view({"post": "create"}), name="api-order-create"
    ),
]
