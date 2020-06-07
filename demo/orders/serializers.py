from rest_framework import serializers
from rest_framework.validators import (
    UniqueTogetherValidator, UniqueForDateValidator
)
from .models import Order, Table


class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('id', 'date_order', 'reservation',)

        validators = [
            # UniqueTogetherValidator(
            #     queryset=Order.objects.all(),
            #     fields=['date_order', 'reservation'],
            #     message='Столик уже заказан на эту дату'
            # ),
            UniqueForDateValidator(
                queryset=Order.objects.all(),
                field='reservation',
                message='Этот столик уже заказан',
                date_field='date_order'
            ),
        ]


class TableSerializer(serializers.ModelSerializer):
    tables = serializers.StringRelatedField(many=True)

    class Meta:
        model = Table
        fields = (
            'id', 'number', 'seats', 'shape', 'tables',
            'center_x', 'center_y', 'width', 'length'
        )
        extra_kwargs = {
            'center_x': {'max_digits': 5, 'decimal_places': 2},
            'center_y': {'max_digits': 5, 'decimal_places': 2},
            'width': {'max_digits': 5, 'decimal_places': 2},
            'length': {'max_digits': 5, 'decimal_places': 2},
        }
