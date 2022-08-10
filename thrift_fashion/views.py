from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'thrift_fashion/home.html')

def about(request):
    return render(request, 'thrift_fashion/about.html')

def products(request):
    return render(request, 'thrift_fashion/products.html')

def product_detail(request):
    return render(request, 'thrift_fashion/product_details.html')

def contact(request):
    return render(request, 'thrift_fashion/contact.html')