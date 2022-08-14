from django.contrib import admin
from .models import Cart_Item, Cart

# Register your models here.
@admin.register(Cart_Item)
class Cart_ItemAdmin(admin.ModelAdmin):
   pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
   pass