from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm

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
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']        
        ContactForm.objects.create(firstname=firstname, lastname=lastname, email=email, subject=subject, message=message)
        messages.success(request, 'Your message has been sent!')
        return redirect(request.META.get('HTTP_REFERER'))
    return render(request, 'thrift_fashion/contact.html')