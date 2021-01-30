import requests
import json
from paysafe.utils import paysafe_config
class UserController():
    def __init__(self,user):
        self.url="https://api.test.paysafe.com/paymenthub/v1/customers"
        self.user=user

    def get_customer_id(self):
        body = {
            "merchantCustomerId": self.user.merchantCustomerId,
            "locale": self.user.locale,
            "firstName": self.user.firstName,
            "lastName": self.user.lastName,
            "dateOfBirth": self.user.dateOfBirth,
            "email": self.user.email,
            "phone": self.user.cellPhone,
            "ip": self.user.ip,
            "gender": self.user.gender,
            "nationality": self.user.nationality,
            "cellPhone": self.user.cellPhone
        }

        headers = {
            'Content-Type':'application/json',
            'Authorization':'Basic '+ paysafe_config.PRIVATE_KEY_BASE64,
            'Simulator':"EXTERNAL"
        }
        res = requests.post(self.url, data = json.dumps(body),headers=headers)
        res_body_dict = json.loads(res.text)
        print(res_body_dict)
        return res_body_dict['id']

