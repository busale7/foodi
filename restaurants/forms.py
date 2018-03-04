from django import forms

from .models import Business ,Items #importing the class Business from models.py
from django.contrib.auth.models import User #importing User from models


class BusinessesForm(forms.ModelForm) :
	class Meta:
		model= Business
		fields ='__all__'
#['name', 'description','opening_time', 'closing_time','add_date','image']
		
		widgets= {
			"add_date" : forms.DateInput(attrs={"type": "date"})

		}
class SignupForm(forms.ModelForm):
	class Meta:
		model= User
		fields =['username','email','first_name','last_name','password']
		widgets={
			"password":forms.PasswordInput()

		}

class LoginForm(forms.Form) :
	username = forms.CharField(required=True)
	password = forms.CharField(required=True , widget=forms.PasswordInput())


class ItemForm(forms.ModelForm) :
	class Meta:
		model= Items
		fields ='__all__'
		exclude = ["restaurant"]
#['item_name', 'descrip','restaurant', 'price','add_date']
		
		widgets= {
			"add_date" : forms.DateInput(attrs={"type": "date"})

		}