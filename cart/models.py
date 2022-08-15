from itertools import product
from django.db import models
from accounts.models import User
from products.models import Product

# Create your models here.
class Cart_Item(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   ordered = models.BooleanField(default=False)
   product = models.ForeignKey(Product, on_delete=models.CASCADE)
   quantity = models.IntegerField(default=1)

   def __str__(self):
      return f"{self.quantity} of {self.product.product_name }"

   def get_total_product_price(self):
      return self.quantity * self.product.price

   def get_total_discount_price(self):
      return self.quantity * self.product.discount_price

   def get_amount_saved(self):
      return self.get_total_product_price() - self.get_total_discount_price()

   def get_final_price(self):
      if self.product.discount_price:
         return self.get_total_discount_price()
      return self.get_total_product_price()

   class Meta:
      verbose_name = 'Cart Item'
      verbose_name_plural = 'Cart Items'

class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   items = models.ManyToManyField(Cart_Item, blank=True, related_name="cart_items")
   ordered = models.BooleanField(default=False)
   added_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.username

   def get_total(self):
      total = 0
      for cart_item in self.items.all():
         total += cart_item.get_final_price()
      return total