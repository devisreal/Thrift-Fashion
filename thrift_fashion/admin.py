from django.contrib import admin
from . import models


@admin.register(models.ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
   pass
