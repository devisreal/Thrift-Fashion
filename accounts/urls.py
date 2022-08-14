from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
   path('login/', views.login, name='login'),
   path('logout/', views.logout, name='logout'),
   path('settings/', views.user_settings, name='user_settings' ),
   path('register/', views.register, name='register'),
]