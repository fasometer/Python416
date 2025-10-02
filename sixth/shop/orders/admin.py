from django.contrib import admin
from .models import Order


# Register your models here.

class OrderAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'status')
    fields = ('id', 'created',
              ('first_name', 'last_name'),
              ('email', 'address'),
              'basket_history', 'status', 'initiator')
    readonly_fields = ('id', 'created',)


admin.site.register(Order, OrderAdmin)
