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
def register(request):
    if(request.method=="POST"):
        request_post=request.POST.copy() # to make it mutable
        request_post["merchantCustomerId"] = ""
        request_post["customerId"] = ""
        # Get merchantCustomerId
        new_merchantCustomerId = MerchantIDGenerator().get_merchant_id()
        # Get customerId
        new_user=User(
            merchantCustomerId=new_merchantCustomerId,
            firstName=request.POST["firstName"],
            middleName=request.POST["middleName"],
            lastName=request.POST["lastName"],
            DD=request.POST["DD"],
            YYYY=request.POST["YYYY"],
            MM=request.POST["MM"],
            email=request.POST["email"],
            phone=request.POST["phone"]
            )
        userController = UserController(new_user)
        customerId = userController.get_customer_id()
        request_post["merchantCustomerId"] = new_merchantCustomerId
        request_post["customerId"] = customerId
        request.POST = request_post

        # Save data to DB
        form=CustomerForm(data = request.POST)
        if form.is_valid():
            form.save()
        else:
            # form is invalid
            pass
        
        request.session['customerId'] = customerId
        messages.success(request, ('Your form has been submitted successfully!'))
        return HttpResponseRedirect('checkout')
    return render(request,'register.html',{})
