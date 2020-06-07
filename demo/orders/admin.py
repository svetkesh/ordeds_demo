from django.contrib import admin

# Register your models here.

from .models import Table, Order

admin.site.register(Order)
admin.site.register(Table)
