from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from .forms import EditProfileForm, AddressForm


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
               return redirect('accounts:user_settings')
            else:                
               messages.warning(request, 'Account is not active')
               return render(request, 'accounts/login.html')                         
         else:
            messages.error(request, 'Please enter valid details')
            return render(request, 'accounts/login.html')
   return render(request, 'accounts/login.html')

# ! Register Users View
def register(request):
   if request.method == 'POST':
      # Get form data
      username = request.POST['username']
      firstname = request.POST['firstname']
      lastname = request.POST['lastname']
      email = request.POST['email']
      contact_phone = request.POST['contact_phone']
      password = request.POST['password1']
      confirm_password = request.POST['password2']

      # Check if both passwords are identical
      if password == confirm_password:
         # Check if user's username exists in the database
         if User.objects.filter(username=username).exists():
            messages.error(request, 'Username Taken')
            return redirect('accounts:register')
         else:
            # Check if user's email exists in the database
            if User.objects.filter(email=email).exists():
               messages.error(request, 'Email already used')
               return redirect('accounts:register')
            else:
               # Create new user
               user = User.objects.create_user(
                  username=username,
                  first_name=firstname,
                  last_name=lastname,
                  email=email,
                  password=password,
                  contact_phone=contact_phone
               )
               # Log that new user in
               user_login(request, user)
               # Checks if the user is not a staff
               if not user.is_staff:
                  messages.success(
                     request, 'Account created successfully, please complete your profile'
                  )
               # if user is not a staff te user is redirected to complete his/her profile
               return redirect('accounts:user_settings')
      else:
         # If both password entered by the user don't match return erroe massage
         messages.error(request, 'Passwords do not match')
         return redirect('register')
   return render(request, 'accounts/register.html')


# ! Setting View for Users
# * @login_required makes sure a user is logged in before accessing a page
@login_required
def user_settings(request):
   if request.method == 'POST':
         edit_profile_form = EditProfileForm(request.POST or None, request.FILES, instance=request.user)
         address_form = AddressForm(request.POST)
         if edit_profile_form.is_valid():
            edit_profile_form.save()
            messages.success(request, 'Profile updated successfully')
            return redirect('accounts:user_settings')

         if address_form.is_valid():
            instance = address_form.save(commit=False)
            instance.user = request.user         
            instance.save()
            messages.success(request, 'Testimony successful, thank you 🙂')
            return redirect('accounts:user_settings')
   else:
      edit_profile_form = EditProfileForm(instance=request.user)
      address_form = AddressForm()
   context = {
        'edit_profile_form': edit_profile_form,
         'address_form': address_form
   }
   return render(request, 'accounts/settings.html', context)


# ! Logout View for Users
# * @login_required makes sure a user is logged in before accessing a page
@login_required
def logout(request):
   # Logout user
   user_logout(request)
    # Return success message
   messages.success(request, 'See you soon 🙂')
    # Redirect to home page
   return redirect(request.META.get('HTTP_REFERER'))
