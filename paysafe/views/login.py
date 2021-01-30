from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from paysafe.utils import paysafe_config
from paysafe.utils.merchant_id_generator import MerchantIDGenerator
from paysafe.utils.merchant_ref_number_generator import MerchantRefNumberGenerator
import json
from django.views.decorators.csrf import csrf_exempt
from paysafe.models import Customer
from paysafe.forms import CustomerForm
from django.contrib import messages
from paysafe.user import User
from paysafe.controllers.user_controller import UserController
from paysafe.controllers.token_controller import TokenController
from paysafe.controllers.payment_controller import PaymentController

def login(request):
    # Handle post request and route to checkout page
    # send customerID to checkout page
    if(request.method=="POST"):
        all_customers = Customer.objects.all()
        print(request.POST)
        for i in all_customers:
            if i.email==request.POST["email"]:
                if i.password==request.POST["password"]:
                    # Correct password
                    print("user Logged in")
                    request.session['customerId']=i.customerId
                    print(i.customerId)
                    break
                else:
                    #incorrect password
                    pass

        #request.session['customerId']="84fc3de7-d84c-4ce3-b275-0f962c448529"
        return HttpResponseRedirect('checkout')
    return render(request,'login.html',{})