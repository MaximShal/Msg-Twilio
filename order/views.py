from django.shortcuts import render, redirect
from django.utils import timezone
from django.views import View

from order.forms import OrderForm
from order.serializers import OrderSerializer
from order.models import Order


class OrderCreateView(View):
    template_name = "order_form.html"

    def get(self, request):
        return render(request, self.template_name, {"form": OrderForm()})

    def post(self, request):
        form = OrderForm(
            {
                "start_timestamp": int(
                    timezone.datetime.timestamp(
                        timezone.datetime.strptime(
                            request.POST["start_timestamp"], "%Y-%m-%dT%H:%M"
                        )
                    )
                ),
                "end_timestamp": int(
                    timezone.datetime.timestamp(
                        timezone.datetime.strptime(
                            request.POST["end_timestamp"], "%Y-%m-%dT%H:%M"
                        )
                    )
                ),
                "user_email": request.POST["user_email"],
                "user_name": request.POST["user_name"],
            }
        )
        if form.is_valid():
            order_serializer = OrderSerializer(data=form.cleaned_data)
            if order_serializer.is_valid():
                order = order_serializer.save()
                return redirect("order-detail", slug=order.slug)

            return render(
                request,
                self.template_name,
                {"form": form, "errors": order_serializer.errors},
            )

        return render(request, self.template_name, {"form": form})


class OrderRetrieveView(View):
    queryset = Order.objects.all()
    template_name = "order_detail.html"

    def get(self, request, **kwargs):
        order = Order.objects.get(slug=kwargs.get("slug", None))
        return render(request, self.template_name, {"order": order})
