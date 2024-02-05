from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ("slug",
                    "start_timestamp",
                    "end_timestamp",
                    "user_email",
                    "user_name",
                    "cell_id",
                    "reminded",
                    "created_at")
