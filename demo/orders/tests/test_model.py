from datetime import date

today = date.today()


from django.test import TestCase
# from django.urls import reverse

from orders.models import Order, Table


class OrderTests(TestCase):
    today = date.today()

    def setUp(self):
        Order.objects.create(
            date_order=today
        )
