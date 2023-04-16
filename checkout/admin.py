from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total')


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number', 'date',
                       'delivery_cost', 'order_total',
                       'grand_total',)

    fields = ('order_number', 'date', 'full_name',
              'email', 'phone_number', 'country',
              'postcode', 'town_or_city', 'streetaddress1',
              'streetaddress2', 'county', 'delivery_cost',
              'order_total', 'grand_total')

    list_display = ('order_number', 'date', 'full_name',
                    'order_total', 'delivery_cost', 'grand_total')

    ordering = ('-date')


"""

Fields keeps the model order as Django will try to
change it based on the read_only fields.

list_display restricts the columns that show up in the order list
to only a few key items

"""
