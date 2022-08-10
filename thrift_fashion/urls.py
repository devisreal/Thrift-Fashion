from django.urls import path
from . import views

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),
   path('products/', views.products, name='products'),
   path('product_detail/', views.product_detail, name='product_detail'),
   path('contact/', views.contact, name='contact'),   
]