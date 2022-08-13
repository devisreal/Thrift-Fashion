from django.db import models
from accounts.models import User
from products.models import Product

# Create your models here.
class Cart(models.Model):
   user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_items')
   products = models.ManyToManyField(Product, blank=True)   
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.user.username