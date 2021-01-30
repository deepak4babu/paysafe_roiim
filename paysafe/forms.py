from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
        # Any data passed to Memberform will be input data for below model
        model = Customer
        fields = [
            'firstName',
            'middleName',
            'lastName',
            'DD',
            'MM',
            'YYYY',
            'street',
            'street2',
            'city',
            'state',
            'zipcode',
            'phone',
            'email',
            'password',
            'reEnterPassword',
            'merchantCustomerId',
            'customerId'
            ]