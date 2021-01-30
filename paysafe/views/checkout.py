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

def checkout(request):
    customerId = ""
    new_merchantRefNum=""
    customer_dict = {}
    all_customers = Customer.objects.all()
    # Adding common keys and values to dict
    customer_dict["currency"]="USD"
    customer_dict["environment"]="TEST"
    customer_dict["displayPaymentMethods"]=["card"]
    customer_dict["paymentMethodDetails"]={}
    customer_dict["canEditAmount"]=True
    customer_dict["merchantDescriptor"]={"dynamicDescriptor": "XYZ","phone": "9876543210"}
    customer_dict["locale"]="en_US"

    # if customerId is in session, then the page is rendered by
    # login or register
    if("customerId" in request.session.keys()):
        customerId = request.session['customerId']
        #print(request.session['customerId'])
        customer_dict["customerId"]=customerId
    
        # Generate SingleUseCustomerToken here
        # Create a merchantRefNum for the checkout
        new_merchantRefNum = MerchantRefNumberGenerator().get_merchant_ref_number()
        #print("CustomerId sent to token Controller",customerId)
        tokenController = TokenController(customerId,new_merchantRefNum)
        singleUseCustomerToken = tokenController.get_single_use_customer_token()

        # Add customerId and SingleUseCustomerToken in the payload
        customer_dict["customerId"]=customerId
        customer_dict["singleUseCustomerToken"]=singleUseCustomerToken
        customer_dict["merchantRefNum"]=new_merchantRefNum
        request.session['merchantRefNum']=new_merchantRefNum

        # Get details of the customer from DB
        for i in all_customers:
            if(i.customerId==customerId):
                customer_dict["customer"]={
                    "firstName": i.firstName,
                    "lastName": i.lastName,
                    "email": i.email,
                    "phone": i.phone,
                    "dateOfBirth": {
                        "day": i.DD,
                        "month": i.MM,
                        "year": i.YYYY
                        }
                    }
                customer_dict["billingAddress"]={
                    "nickName": i.firstName+i.lastName,
                    "street": i.street,
                    "street2": i.street2,
                    "city": i.city,
                    "zip": i.zipcode,
                    "country": "US",
                    "state": i.state
                }
                break

        #Get amount to be paid from user. Hard-coded for now
        customer_dict_json=json.dumps(customer_dict)
        #print(customer_dict_json)
        return render(request,'checkout.html',{'PUBLIC_API_KEY':paysafe_config.PUBLIC_KEY_BASE64,'customer_dict':customer_dict_json})
