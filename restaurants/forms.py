from django import forms

from .models import Business #importing the class Business from models.py

class BusinessesForm(forms.ModelForm) :
	class Meta:
		model= Business
		fields =['name', 'description','opening_time', 'closing_time']
		