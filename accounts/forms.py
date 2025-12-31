
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name','username' , 'email', 'password1', 'password2']
       
       
        widgets = {
    'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
    'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'username': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
  'password1' : forms.TextInput(attrs={'class': 'form-control', 'required': True}),
   'password2': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
  
}




class User_profile_update(forms.ModelForm):
    class Meta:
        model = User
        fields = [ 'first_name', 'last_name', 'email']
        
       
       
        widgets = {
    'email': forms.EmailInput(attrs={'class': 'form-control', 'required': True}),
    'first_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
    'last_name': forms.TextInput(attrs={'class': 'form-control', 'required': True}),
   
  
}

           
        










class UpdateUserForm(forms.ModelForm):
    

    class Meta:
        model = User
        fields = [ 'email' , 'first_name', 'last_name']
        widgets = {
            
            'email': forms.TextInput(attrs={'class': 'form-control'}),
           'first_name': forms.TextInput(attrs={'class': 'form-control'}),
           'last_name': forms.TextInput(attrs={'class': 'form-control'}),
        }

