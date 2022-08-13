from django.shortcuts import render

# Create your views here.
def products(request):
   return render(request, 'products/products.html')

def product_detail(request):
   return render(request, 'products/product_detail.html')


def male_products(request):
   return render(request, 'products/product_males.html')

def female_products(request):
   return render(request, 'products/product_females.html')

def kids_products(request):
   return render(request, 'products/product_kids.html')

def search_products(request):
   return render(request, 'products/search_products.html')