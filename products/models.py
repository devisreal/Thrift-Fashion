from django.db import models
from django.template.defaultfilters import slugify

# Create your models here.
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