import time
class MerchantRefNumberGenerator():
    def __init__(self):
        pass


    @staticmethod
    def get_merchant_ref_number():
        random_id="dee"+str(int(time.time()))
        return random_id