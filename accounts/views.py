from django.shortcuts import render, redirect
from django.contrib import messages, auth
# from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout


# Create your views here.
def login(request):
   if request.user.is_authenticated:
      messages.warning(request, 'You are already logged in!')
      return redirect('home')
   else:
      if request.method == 'POST':
         username = request.POST['username']
         password = request.POST['password']

         user = authenticate(username=username, password=password)

         if user:
            if user.is_active:
               user_login(request, user)
               messages.success(request, f'Welcome {username}')
               return redirect('home')
            else:                
               messages.warning(request, 'Account is not active')
               return render(request, 'account/login.html')                         
         else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'account/login.html')
   return render(request, 'accounts/login.html')


def register(request):
   return render(request, 'accounts/register.html')