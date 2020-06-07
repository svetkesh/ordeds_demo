from datetime import date
from django.db import models

from .validators import validate_date_order_not_in_past

# Create your models here.


class Table(models.Model):
    RECTANGLE = 'REC'
    OVAL = 'OVL'
    TABLE_SHAPE_CHOICES = [
        (RECTANGLE, 'Прямоугольный, квадратный'),
        (OVAL, 'Овальный, круглый'),
    ]

    number = models.IntegerField(blank=False)
    seats = models.IntegerField()
    shape = models.CharField(
        max_length=3,
        choices=TABLE_SHAPE_CHOICES,
        default=RECTANGLE,
    )
    center_x = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    center_y = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    width = models.DecimalField(max_digits=5, decimal_places=2, default=0)
    length = models.DecimalField(max_digits=5, decimal_places=2, default=0)

    class Meta:
        ordering = ['number']

    def __str__(self):
        return 'Стол_{}'.format(self.number)


class Order(models.Model):
    date_order = models.DateField(
        default=date.today,
        validators=[validate_date_order_not_in_past]
    )
    reservation = models.ForeignKey(
        Table,
        related_name='tables',
        on_delete=models.CASCADE,
    )

    class Meta:
        unique_together = ("date_order", "reservation")
        ordering = ['date_order']

    def __str__(self):
        return '{} заказан на {}'.format(self.reservation, self.date_order)
