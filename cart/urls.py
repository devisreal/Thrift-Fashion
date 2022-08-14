from django.urls import path
from . import views


app_name = 'cart'

urlpatterns = [
   path('', views.cart, name='cart'),
   path('cart/add/<slug:slug>/', views.add_to_cart, name='add'),
   path('cart/remove/<slug:slug>/', views.remove_from_cart, name='remove'),
]