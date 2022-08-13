from django.contrib import admin
from . import models

# Register your models here.
@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display = ('name',)


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
   list_display = ('product_name', 'category', 'price', 'no_in_stock')
