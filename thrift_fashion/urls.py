from django.urls import path
from . import views
from cart.views import cart
from products.views import product_detail, products, female_products, kids_products, male_products, search_products

urlpatterns = [
   path('', views.home, name='home'),
   path('about/', views.about, name='about'),

   path('products/', products, name='products'),
   path('product_detail/<slug:slug>/', product_detail, name='product_detail'),
   path('products/men/', male_products, name='product_male'),
   path('products/women/', female_products, name='product_female'),
   path('products/search/', search_products, name='search_products' ),
   path('products/kids/', kids_products, name='product_kids'),

   path('contact/', views.contact, name='contact'),   

   path('cart/', cart, name='cart'),
   
]