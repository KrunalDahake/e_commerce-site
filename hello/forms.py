from cProfile import label
from tkinter import Widget
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,UserChangeForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django import forms
from django.utils.translation import gettext,gettext_lazy as _
from .models import Customer
from django.contrib.auth import password_validation

class SignUpForm(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Password Confirm',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','first_name','last_name','email']
        labels={'email':'Email'}
        widgets={'username':forms.EmailInput(attrs={'class':'form-control'}),
                 'first_name':forms.TextInput(attrs={'class':'form-control'}),
                 'last_name':forms.TextInput(attrs={'class':'form-control'}),
                 'email':forms.EmailInput(attrs={'class':'form-control'}),
                 }

class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 

# class UserProfileForm(UserChangeForm):
#     password=None
#     class Meta:
#         model=User
#         fields=['username','first_name','last_name','email','date_joined','last_login']
#         labels={'email':'Email'}
#         widgets={'username':forms.TextInput(attrs={'class':'form-control'}),
#                  'first_name':forms.TextInput(attrs={'class':'form-control'}),
#                  'last_name':forms.TextInput(attrs={'class':'form-control'}),
#                  'email':forms.EmailInput(attrs={'class':'form-control'}),
#                  'date_joined':forms.DateTimeInput(attrs={'class':'form-control'}),
#                  'last_login':forms.DateTimeInput(attrs={'class':'form-control'}),
                #  }
class CustomerProfileForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','pincode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),
                 'locality':forms.TextInput(attrs={'class':'form-control'}),
                 'city':forms.TextInput(attrs={'class':'form-control'}),
                 'state':forms.Select(attrs={'class':'form-control'}),
                 'pincode':forms.NumberInput(attrs={'class':'form-control'})}                  
 
class MypasswordChangeForm(PasswordChangeForm):
    old_password=forms.CharField(label=_('Old Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','autofocus':True,'class':'form-control'}))        
    new_password1=forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())        
    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password','class' : 'form-control'}))
    

class MypasswordResetForm(PasswordResetForm):
    email=forms.EmailField(label=('Email'),max_length=255,widget=forms.EmailInput(attrs={'autocomplete':'email','class':'form-control'}))


class MysetPasswordForm(SetPasswordForm):
    new_password1=forms.CharField(label=_('New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete':'new-password','class':'form-control'}),help_text=password_validation.password_validators_help_text_html())
            
    new_password2=forms.CharField(label=_('Confirm New Password'),strip=False,widget=forms.PasswordInput(attrs={'autocomplete' : 'new-password','class' : 'form-control'}))    
                