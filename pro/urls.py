from django.contrib import admin
from django.urls import path
from pip._internal.models import index

from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('view/', views.view ,name='view'),
    path('home1/', views.home1, name='home1'),
    path('logout/', views.custom_logout, name='logout'),
    path('cart/', views.cart_view, name='cart'),
    path('thank/', views.thank, name='thank'),
    path('Addbook/', views.Addbook, name='Addbook'),
    path('whereabouts/', views.whereabouts, name='whereabouts'),
    path('upi_payment/', views.upi_payment, name='upi'),
    path('about_us/', views.about_us, name='AboutUs'),
    path('feedback/', views.feedback, name='feedback'),
    path('contactus/', views.contactus, name='contactus'),
]