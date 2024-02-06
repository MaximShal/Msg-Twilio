from django.contrib import admin
from order.models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (
        "slug",
        "get_convert_start_timestep",
        "get_convert_end_timestep",
        "user_email",
        "user_name",
        "cell_id",
        "reminded",
        "created_at",
    )

    @staticmethod
    def get_convert_end_timestep(obj):
        return obj.end_datetime()

    @staticmethod
    def get_convert_start_timestep(obj):
        return obj.start_datetime()
