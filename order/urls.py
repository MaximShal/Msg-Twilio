from django.urls import path
from order.views import OrderCreateView, OrderRetrieveView

urlpatterns = [
    path("<slug:slug>/", OrderRetrieveView.as_view(), name="order-detail"),
    path("", OrderCreateView.as_view(), name="orders"),
]
