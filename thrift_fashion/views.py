from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactForm
from products.models import Product

# Create your views here.
def home(request):
    latest_products = Product.objects.all().order_by('-id')[:4]

    context = {
        'latest_products': latest_products,
    }

    return render(request, 'thrift_fashion/home.html', context)

def about(request):
    return render(request, 'thrift_fashion/about.html')

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