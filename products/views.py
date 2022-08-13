from django.shortcuts import render, get_object_or_404
from .models import Product, Category

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
   return render(request, 'products/product_males.html')

def female_products(request):
   return render(request, 'products/product_females.html')

def kids_products(request):
   return render(request, 'products/product_kids.html')

def search_products(request):
   

   return render(request, 'products/search_products.html')