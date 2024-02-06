import requests
from django.utils import timezone
from rest_framework import serializers
from mt.settings import CELL_ID_LINK
from order.models import Order


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        exclude = ("cell_id",)

    def validate(self, data):
        start_timestamp = data.get("start_timestamp")
        end_timestamp = data.get("end_timestamp")

        if end_timestamp <= start_timestamp or end_timestamp <= int(
            timezone.now().timestamp()
        ):
            raise serializers.ValidationError(
                "End timestamp must be greater than start timestamp and current time."
            )

        return data

    def create(self, validated_data):
        response = requests.get(CELL_ID_LINK)
        random_number = response.json()[0].get("random", None)
        validated_data["cell_id"] = random_number
        order = super().create(validated_data)
        return order
