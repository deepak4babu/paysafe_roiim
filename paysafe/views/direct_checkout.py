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

def direct_checkout(request):
    if(request.method== "POST"):
        # save customer_payload in session to use to register
        #customer_payload=request.POST.copy()
        #request.session['customer_payload']=customer_payload 
        pass
    else:
        new_merchantRefNum = MerchantRefNumberGenerator().get_merchant_ref_number()
        request.session['merchantRefNum']=new_merchantRefNum
        return render(request,'direct_checkout.html',{'PUBLIC_API_KEY':paysafe_config.PUBLIC_KEY_BASE64,"merchantRefNum":new_merchantRefNum})
