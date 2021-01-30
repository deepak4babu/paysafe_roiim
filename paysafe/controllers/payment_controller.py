from paysafe.utils import paysafe_config
import requests
import json
class PaymentController():
    def __init__(self,merchant_ref_num,amount,payment_handle_token,currency_code,customer_id,merchant_customer_id):
        self.url = "https://api.test.paysafe.com/paymenthub/v1/payments"
        self.merchant_ref_num = merchant_ref_num
        self.amount = amount
        self.payment_handle_token = payment_handle_token
        self.currency_code = currency_code
        self.customer_id=customer_id
        self.merchant_customer_id=merchant_customer_id
    
    def process_payment(self):
        #print("merchant_ref_num is ",self.merchant_ref_num)
        body={
            "merchantRefNum": self.merchant_ref_num,
            "amount": self.amount,
            "currencyCode": self.currency_code,
            "dupCheck": "true",
            "settleWithAuth": "false",
            "paymentHandleToken": self.payment_handle_token,
            "customerIp": "172.0.0.1",
            "description": "Magazine subscription"
            }
        if self.customer_id!="":
            body["customerId"]=self.customer_id
            #print("At PaymentController added customer_id to body to Add card details", body["customerId"])
        elif self.merchant_customer_id!="":
            body["merchantCustomerId"]=self.merchant_customer_id

        headers = {
            'Content-Type':'application/json',
            'Authorization':'Basic '+ paysafe_config.PRIVATE_KEY_BASE64,
            'Simulator':"EXTERNAL"
        }
        res = requests.post(self.url, data = json.dumps(body),headers=headers)
        res_body_dict = json.loads(res.text)
        return res_body_dict