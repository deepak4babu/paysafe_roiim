import requests
import json
from paysafe.utils import paysafe_config
class TokenController():
    def __init__(self,customer_id,merchant_ref_no):
        self.customer_id=customer_id
        self.merchant_ref_no=merchant_ref_no
        self.url="https://api.test.paysafe.com/paymenthub/v1/customers/"+customer_id+"/singleusecustomertokens"
    
    def get_single_use_customer_token(self):
        body = {
            "merchantRefNum":self.merchant_ref_no,
            "paymentTypes": ["CARD"]
        }

        headers = {
            'Content-Type':'application/json',
            'Authorization':'Basic '+ paysafe_config.PRIVATE_KEY_BASE64,
            'Simulator':"EXTERNAL"
        }
        res = requests.post(self.url, data = json.dumps(body),headers=headers)
        #print(res.text)
        # convert json to dict
        res_body_dict = json.loads(res.text)
        #print(res_body_dict)
        return res_body_dict['singleUseCustomerToken']