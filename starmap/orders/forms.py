from django import forms
from .models import OrderPdf, OrderPic
from django.utils.translation import gettext as _

class OrderPdfForm(forms.ModelForm):
    class Meta:
        model = OrderPdf    
        fields = ['email', 'first_name', 'last_name', 'phone']


class OrderPicForm(forms.ModelForm):
    class Meta:
        model = OrderPic
        fields = ['address', 'city', 'country', 'postal_index', 
                  'email', 'first_name', 'last_name', 'phone']
