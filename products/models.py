from django.db import models
from django.template.defaultfilters import slugify
from cloudinary.models import CloudinaryField
from django.core.validators import FileExtensionValidator


class Category(models.Model):
   name = models.CharField(max_length=50)
   slug = models.SlugField(max_length=50, unique=True, blank=True, null=True)

   def __str__(self):
      return self.name

   class Meta:
      verbose_name_plural = "Categories"

   def save(self, *args, **kwargs):
      self.slug = slugify(self.name)
      super().save(*args, **kwargs)





class Product(models.Model):
   size = (
      ('S', 'S'),
      ('M', 'M'),
      ('L', 'L'),
      ('XL', 'XL'),
      ('XXL', 'XXL'),
      ('XXXL', 'XXXL'),
   )
   product_name = models.CharField(max_length=300)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)   
   description = models.TextField(blank=True, null=True)
   size = models.CharField(max_length=10, choices=size)
   brand = models.CharField(max_length=50, blank=True, null=True)
   price = models.DecimalField(max_digits=10, decimal_places=2)
   discount_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
   no_in_stock = models.IntegerField(default=1)
   # size =
   product_image_1 = CloudinaryField(
      'image',      
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg'
            ]
         )
      ]
   )
   product_image_2 = CloudinaryField(
      'image',
      blank=True,
      null=True,
      validators=[
         FileExtensionValidator(
            allowed_extensions=[
               'png', 'jpg', 'jpeg'
            ]
         )
      ]
   )
   slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)
   date_posted = models.DateTimeField(auto_now_add=True)
   date_updated = models.DateTimeField(auto_now=True)

   def __str__(self):
      return self.product_name

   def save(self, *args, **kwargs):
      self.slug = slugify(self.product_name)
      super().save(*args, **kwargs)

   class Meta:
      verbose_name_plural = "Products"

   

