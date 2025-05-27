from django.contrib import admin
from .models import Table, Product, Order
from ordering.models import OrderProduct

# Register your models here.
admin.site.register(Table)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderProduct)

