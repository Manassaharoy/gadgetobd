from django.contrib import admin

# Register your models here.
from django.contrib import admin
from App_Order.models import Cart, Order

# Register your models here.

admin.site.register(Cart)
admin.site.register(Order)
