from django import forms
from .models import *
from products.models import *


class Buy_form(forms.ModelForm):
    class Meta:
        model=Buy
        fields=[
            'cust_name',
            'product_id',
        ]