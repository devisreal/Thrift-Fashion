from django.contrib import admin
from .models import User, Address, CreditCardDetails
# Register your models here.
@admin.register(User)
class UserAdmin(admin.ModelAdmin):
   list_display = ('username', 'email', 'first_name', 'last_name')
   search_fields = ('username', 'email', 'first_name', 'last_name')

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
   pass

@admin.register(CreditCardDetails)
class CreditCardDetailsAdmin(admin.ModelAdmin):
   pass