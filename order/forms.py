
from.models import Order








from django import forms


class OrderForm(forms.ModelForm):
    

    class Meta:
        model = Order
        fields = [ 'email' , 'first_name', 'last_name',
                  'phone',
                  'address_line1',
                  'state',
                  'city'
                 
     
            ]
        widgets = {
    'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
    'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'phone': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'address_line1': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'city': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'state': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
}
        
