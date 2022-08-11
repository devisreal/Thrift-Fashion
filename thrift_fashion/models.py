from django.db import models

# Create your models here.
class ContactForm(models.Model):
   firstname = models.CharField(max_length=100)
   lastname = models.CharField(max_length=100)
   email = models.EmailField(max_length=50)
   subject = models.CharField(max_length=100)
   message = models.TextField()
   created_at = models.DateTimeField(auto_now_add=True)

   def __str__(self):
      return f'{self.firstname} on {self.created_at}'