import time
class MerchantIDGenerator():
    def __init__(self):
        pass


    @staticmethod
    def get_merchant_id():
        random_id=int(time.time())
        return "roiim"+str(random_id)
