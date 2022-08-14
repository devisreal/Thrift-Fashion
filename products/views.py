from unicodedata import category
from django.shortcuts import render, get_object_or_404
from products.models import Product
from django.contrib import messages
from django.db.models import Q

# Create your views here.
def products(request):
   products = Product.objects.all()

   context = {
      'products': products
   }
   return render(request, 'products/products.html', context)

def product_detail(request, slug):
   product = get_object_or_404(Product, slug=slug)
   context = {
      'product': product
   }
   return render(request, 'products/product_detail.html', context)


def male_products(request):
   men_products = Product.objects.filter(category__name='Men')
   context = {
      'men_products': men_products
   }
   return render(request, 'products/product_males.html', context)

def female_products(request):
   women_products = Product.objects.filter(category__name='Women')
   context = {
      'women_products': women_products
   }
   return render(request, 'products/product_females.html', context)

def kids_products(request):
   kids_products = Product.objects.filter(category__name='Kids')
   context = {
      'kids_products': kids_products
   }
   return render(request, 'products/product_kids.html', context)

def unisex_products(request):
   unisex_products = Product.objects.filter(category__name='Unisex')
   context = {
      'unisex_products': unisex_products
   }
   return render(request, 'products/product_unisex.html', context)

def search_products(request):
   if request.method == "POST":
      search = request.POST['search']
      if search:
         products = Product.objects.filter(
            Q(product_name__icontains=search) | 
            Q(category__name__icontains=search) |
            Q(price__icontains=search) |
            Q(brand__icontains=search) |
            Q(size__icontains=search)            
         )
         if products:            
            return render(request, 'products/search_products.html', {'products': products})
         else:
            return render(request, 'products/search_products.html')
      else:
         messages.error(request, 'Please enter a search term')
         return render(request, 'products/search_products.html')
   context = {
      'products': products
   }
   return render(request, 'products/search_products.html', context)