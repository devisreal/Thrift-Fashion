from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('settings/', views.user_settings, name='user_settings' ),
   path('add_address/', views.add_address, name='add_address' ),
   path('address/delete/<int:id>/', views.delete_address, name='delete_address' ),
   path('add_card/', views.add_card_details, name='add_card_details' ),
   path('card/delete/<int:id>/', views.delete_card_details, name='delete_card_details' ),
   path('register/', views.register, name='register'),
]