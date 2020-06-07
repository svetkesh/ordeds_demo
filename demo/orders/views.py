from django.shortcuts import render
from django.core.mail import send_mail
from django.shortcuts import redirect

from rest_framework import generics

from .models import Order, Table
from .serializers import OrderSerializer, TableSerializer

# Create your views here.


class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        send_mail(
            'Заказ столика {} на {}'.format(
                str(serializer.validated_data['reservation']),
                str(serializer.validated_data['date_order'])
            ),
            'Здравствуйте, Вы заказали столик {} на {}'.format(
                str(serializer.validated_data['reservation']),
                str(serializer.validated_data['date_order'])
            ),
            'super@admin.com',
            ['customer@example.com'],
            fail_silently=False,
        )
        serializer.save()


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class TableList(generics.ListCreateAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


class TableDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerializer


def redirect_index(request):
    return redirect('/orders/')
