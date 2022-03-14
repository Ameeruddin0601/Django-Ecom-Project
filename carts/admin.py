from csv import list_dialects
from django.contrib import admin
from carts.models import Cart, CartItem

class CartAdmin(admin.ModelAdmin):
	list_display = ('cart_id', 'date_added')

class CartItemAdmin(admin.ModelAdmin):
	list_display = ('product', 'cart', 'quantity', 'is_active')

admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
# Register your models here.
