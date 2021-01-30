from django.db import models

# Create your models here.
class Customer(models.Model):
    firstName = models.CharField(max_length=50)
    middleName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    DD = models.IntegerField()
    MM = models.IntegerField()
    YYYY = models.IntegerField()
    street = models.CharField(max_length=50)
    street2 = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    reEnterPassword = models.CharField(max_length=50)
    merchantCustomerId=models.CharField(max_length=50)
    customerId=models.CharField(max_length=100)