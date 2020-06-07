from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
# from . import views
from .views import (
    OrderList, OrderDetail,
    TableList, TableDetail,
    redirect_index
)

urlpatterns = [
    path('', redirect_index),
    path('orders/', OrderList.as_view()),
    path('orders/<int:pk>/', OrderDetail.as_view()),
    path('tables/', TableList.as_view()),
    path('tables/<int:pk>/', TableDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
