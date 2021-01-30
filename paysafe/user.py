class User():
    def __init__(self,merchantCustomerId,firstName,middleName,lastName,DD,YYYY,MM,email,phone):
        self.merchantCustomerId = merchantCustomerId
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.dateOfBirth = {"day":int(DD),"month":int(MM),"year":int(YYYY)}
        self.email = email
        self.cellPhone = phone
        self.gender = "M"
        self.locale="en_US"
        self.ip="172.0.0.1"
        self.nationality= "American"
