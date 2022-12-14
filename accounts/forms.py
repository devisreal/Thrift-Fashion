from django import forms
from typing import Any
from .models import User, Address, CreditCardDetails

class EditProfileForm(forms.ModelForm):
   
   username = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   first_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   last_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   profile_image = forms.ImageField(
      label='',
      required=False,
      widget=forms.FileInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   email = forms.EmailField(
      label='Email',
      widget=forms.EmailInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border'
         }
      ),
   )

   contact_phone = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   
   class Meta:
      model = User
      fields = ('username', 'first_name', 'last_name', 'profile_image','email', 'contact_phone' )      
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(EditProfileForm , self).__init__(*args, **kwargs)

      for fieldname in ('username', 'first_name', 'last_name', 'profile_image','email', 'contact_phone'):
         self.fields[fieldname].help_text = None



class AddressForm(forms.ModelForm):
   
   address_type = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   address_line_1 = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   address_line_2 = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   city = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   state = forms.CharField(
      label='Email',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border'
         }
      ),
   )

   zip_code = forms.CharField(
      label='',
      required=False,
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   
   class Meta:
      model = Address
      fields = ('address_type', 'address_line_1', 'address_line_2', 'city','state', 'zip_code' )
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(AddressForm , self).__init__(*args, **kwargs)

      for fieldname in ('address_type', 'address_line_1', 'address_line_2', 'city','state', 'zip_code'):
         self.fields[fieldname].help_text = None


class Add_Card_Form(forms.ModelForm):
   
   credit_card_types = [
      ('Visa', 'Visa'),
      ('MasterCard', 'MasterCard'),
      ('Verve', 'Verve'),
      ('RuPay', 'RuPay'),
   ]

   credit_card_type = forms.ChoiceField(
      choices=credit_card_types,
      widget=forms.Select(
         attrs={
            'class': 'form-control text-md font-medium mb-3 border',
         }
      )
   )

   credit_card_number = forms.CharField(
      label='',
      widget=forms.NumberInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )

   credit_card_expiry = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )
   
   credit_card_cvv = forms.CharField(
      label='',
      widget=forms.NumberInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )
   
   credit_card_name = forms.CharField(
      label='',
      widget=forms.TextInput(
         attrs={
            'placeholder': '',
            'class': 'form-control font-medium text-md bg-white border',
         }
      )
   )
   
   class Meta:
      model = CreditCardDetails
      fields = ('credit_card_type', 'credit_card_number', 'credit_card_expiry', 'credit_card_cvv', 'credit_card_name' )
   
   def __init__(self, *args: Any, **kwargs: Any) -> None:
      super(Add_Card_Form , self).__init__(*args, **kwargs)

      for fieldname in ('credit_card_type', 'credit_card_number', 'credit_card_expiry', 'credit_card_cvv', 'credit_card_name'):
         self.fields[fieldname].help_text = None