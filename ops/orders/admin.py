from django.contrib import admin
from .models import Customer, Order, MenuItem
from .forms import OrderForm

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    fields = ('name',)

class OrderAdmin(admin.ModelAdmin):
    fields= ('name','customer','menuitems',)

class MenuItemAdmin(admin.ModelAdmin):
    fields = ('name',)

admin.site.register(Customer,CustomerAdmin)
admin.site.register(Order,OrderAdmin)
admin.site.register(MenuItem,MenuItemAdmin)