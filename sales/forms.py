from django.forms import ModelForm, inlineformset_factory
from django import forms
from .models import *
from Inventory.models import Product


class CustomerForm(ModelForm):
    class Meta:
        model=Customer
        fields='__all__'

class SaleForm(ModelForm):
    
    class Meta:
        model = Sales
        fields = '__all__'

class SaleItemForm(ModelForm):
 
    class Meta:
        model=SalesItem
        fields=['product','quantity','total_price',]
        widgets = {
        'total_price': forms.NumberInput(attrs={'readonly': 'readonly'}),
    }

SaleItemFormset=inlineformset_factory(Sales,SalesItem, form=SaleItemForm,extra=1)
