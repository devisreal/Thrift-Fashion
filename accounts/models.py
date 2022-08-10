from django.db import models
from django.core.validators import FileExtensionValidator
from django.contrib.auth.models import AbstractUser
from django.template.defaultfilters import slugify

# Create your models here.
class User(AbstractUser):
   # * The user's profile picture
   profile_image = models.ImageField(
      upload_to='profile_images', 
      default='default_profile.png',
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg'
            ]
         )
      ]
   )
   # * The user's phone number
   contact_phone = models.CharField(max_length=14, blank=True)
   # * The user's slug 
   slug = models.SlugField(null=True, blank=True)

   def __str__(self):
      # * Returns the username of the user
      return f'{self.username}'

   def save(self, *args, **kwargs):
      # * Creates the user's slug from the username
      self.slug = slugify(self.username)
      super().save(*args, **kwargs)

# ? User Profile Model
class Address(models.Model):
   # * The user who owns the profile
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   # * The user's home address
   address_type = models.CharField(max_length=200, blank=True)      
   address_line_1 = models.CharField(max_length=200, blank=True)      
   address_line_2 = models.CharField(max_length=200, blank=True)      
   city = models.CharField(max_length=200, blank=True)      
   state = models.CharField(max_length=200, blank=True)      
   zip_code = models.CharField(max_length=20, blank=True)
   
   def __str__(self):
      return f"{self.user.username}'s Profile"


# ? User Credit Card Details
class CreditCardDetails(models.Model):

   # ? Credit card types 
   credit_card_types = (
      ('Visa', 'Visa'),
      ('MasterCard', 'MasterCard'),
      ('Verve', 'Verve'),
      ('RuPay', 'RuPay'),
   )

   # * The user who owns the credit card details
   user = models.OneToOneField(User, on_delete=models.CASCADE)
   # * The user's credit card type
   credit_card_type = models.CharField(choices=credit_card_types,max_length=20, blank=True)
   # * The user's credit card number
   credit_card_number = models.CharField(max_length=16, blank=True)
   # * The user's credit card expiry date
   credit_card_expiry = models.CharField(max_length=5, blank=True)
   # * The user's credit card CVV
   credit_card_cvv = models.CharField(max_length=3, blank=True)
   # * The user's credit card name
   credit_card_name = models.CharField(max_length=50, blank=True)
   
   
   
   def __str__(self):
      return f"{self.user.username}'s Credit Card Details"
