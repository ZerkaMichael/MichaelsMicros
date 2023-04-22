from django.contrib import admin
from .models import Product
from cart.models import *

# Register your models here.

admin.site.register(Product)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)