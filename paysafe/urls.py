from django.contrib import admin
from django.urls import path
from paysafe.views import home,login,register,checkout,payment,direct_checkout,direct_checkout_register

urlpatterns = [
    path('',home.home,name="home"),
    path('login',login.login,name="login"),
    path('register',register.register,name="register"),
    path('checkout',checkout.checkout,name="checkout"),
    path('payment',payment.payment,name="payment"),
    path('direct_checkout',direct_checkout.direct_checkout,name="direct_checkout"),
    path('direct_checkout_register',direct_checkout_register.direct_checkout_register,name="direct_checkout_register"),
]
