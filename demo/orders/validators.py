from datetime import date
from rest_framework import serializers


def validate_date_order_not_in_past(value):
    today = date.today()
    if value < today:
        raise serializers.ValidationError(
            "Можно заказать столик на сегодня или позже только"
        )
