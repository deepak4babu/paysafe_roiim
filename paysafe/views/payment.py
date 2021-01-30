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

@csrf_exempt
def payment(request):
    if(request.method== "POST"):
        customer_id=""
        new_merchantCustomerId=""
        print("Received Payment handle token")
        checkout_response = json.loads(request.body)
        print(checkout_response)

        # Handle payment here
        if('customerOperation' in checkout_response.keys()):
            # Save card flow
            print("User selected save the card flow")
            if("customerId" in request.session.keys()):
                # Logged In, Send Customer ID with payments
                print("Adding customer id to payment controller",request.session["customerId"])
                customer_id=request.session["customerId"]
                del(request.session["customerId"])
            else:
                print("CustomerID is not present, getting merchant_customer_id")
                # Not Logged In, create Merchant Customer ID
                new_merchantCustomerId = MerchantIDGenerator().get_merchant_id()
                # Save customer_payload to session
                request.session["merchantCustomerId_direct_checkout"]=new_merchantCustomerId
                request.session["customer_payload_direct_checkout"]=checkout_response["customer_payload"].copy()
        paymentController = PaymentController(
            merchant_ref_num=request.session['merchantRefNum'],
            amount=checkout_response["amount"],
            payment_handle_token=checkout_response["paymentHandleToken"],
            currency_code="USD",
            customer_id=customer_id,
            merchant_customer_id=new_merchantCustomerId
            )
        payment_response = paymentController.process_payment()
        payment_response_json=json.dumps(payment_response)
        if new_merchantCustomerId!="" and payment_response["status"]=="COMPLETED" :
            request.session["payment_response_direct_checkout"]=payment_response
        #    return render(request,"direct_checkout_register.html",{})
        
        return HttpResponse(payment_response_json,content_type='application/json')
    return render(request,'home.html',{})
