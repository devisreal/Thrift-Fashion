from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from cart.models import Cart_Item, Cart
from products.models import Product
from django.contrib import messages

@login_required
def cart(request):   
   
   mycart = Cart.objects.get(user=request.user, ordered=False)   
   context = {
      'mycart': mycart,
   }
   return render(request, 'cart/cart.html', context)

@login_required
def add_to_cart(request, slug):
   product = get_object_or_404(Product, slug=slug)
   cart_item, created = Cart_Item.objects.get_or_create(
      product=product,
      user=request.user,
      ordered=False
   )
   cart_qs = Cart.objects.filter(user=request.user, ordered=False)
   if cart_qs.exists():
      cart = cart_qs[0]
      if cart.items.filter(product__slug=product.slug).exists():
         cart_item.quantity += 1
         cart_item.save()      
         messages.info(request, "This item quantity was updated.")
         return redirect(request.META.get('HTTP_REFERER'))
      else:            
         messages.success(request, "This item was added to your cart.")
         cart.items.add(cart_item)
   else:
      cart = Cart.objects.create(user=request.user)
      cart.items.add(cart_item)
      messages.success(request, "This item was added to your cart.")         
   return redirect(request.META.get('HTTP_REFERER'))

@login_required
def remove_from_cart(request, slug):
   product = get_object_or_404(Product, slug=slug)
   cart_qs = Cart.objects.filter(
      user=request.user, ordered=False
   )
   if cart_qs.exists():
      cart = cart_qs[0]
      if cart.items.filter(product__slug=product.slug).exists():
         cart_item = Cart_Item.objects.get_or_create(
            product=product,
            user=request.user,
            ordered=False
         )[0]
         cart.items.remove(cart_item)
         messages.success(request, "This item was removed from your cart.")
         return redirect(request.META.get('HTTP_REFERER'))
      else:
         messages.error(request, "This item is not in your cart")
         return redirect(request.META.get('HTTP_REFERER'))        
   else:
      messages.error(request, 'You do not have an item in your cart')
      return redirect(request.META.get('HTTP_REFERER'))
   