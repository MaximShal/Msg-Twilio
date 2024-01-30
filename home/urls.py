from django.urls import path
from home.views import HomeView, SendSmsView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("send-sms/", SendSmsView.as_view(), name="send-sms"),
]
