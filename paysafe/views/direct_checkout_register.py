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

def direct_checkout_register(request):
    if(request.method== "POST"):
        # use customer_payload_direct_checkout in request session
        request_details = request.POST.copy()
        
        customer_details=request.session["customer_payload_direct_checkout"]
        payment_response=request.session["payment_response_direct_checkout"]
        merchantCustomerId=request.session["merchantCustomerId_direct_checkout"]
        
        # Session cleanup
        del(request.session["customer_payload_direct_checkout"])
        del(request.session["payment_response_direct_checkout"])
        del(request.session["merchantCustomerId_direct_checkout"])
        
        #print(customer_details)
        #print(payment_response)
        #print(request_details)
        #print(merchantCustomerId)

        form_data={"firstName": customer_details["customer"]["firstName"],
            "lastName" : customer_details["customer"]["lastName"],
            "DD" : customer_details["customer"]["dateOfBirth"]["day"],
            "MM" : customer_details["customer"]["dateOfBirth"]["month"],
            "YYYY" : customer_details["customer"]["dateOfBirth"]["year"],
            "street" : customer_details["billingAddress"]["street"],
            "street2" : customer_details["billingAddress"]["street2"],
            "city" : customer_details["billingAddress"]["city"],
            "state" : customer_details["billingAddress"]["state"],
            "zipcode" : customer_details["billingAddress"]["zip"],
            "phone" : customer_details["customer"]["phone"],
            "email" : request_details["email"],
            "password" : request_details["password"],
            "reEnterPassword" : request_details["reEnterPassword"],
            "merchantCustomerId": merchantCustomerId,
            "customerId": payment_response["customerId"],
        }
        print(form_data)


        # Save data to DB
        form=CustomerForm(data = form_data)
        if form.is_valid():
            form.save()
        return render(request,'home.html',{})
    return render(request,'direct_checkout_register.html',{})


