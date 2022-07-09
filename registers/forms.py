

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordResetForm,AuthenticationForm

from django import forms
from django.forms import EmailField,TextInput,PasswordInput,ImageField







class LoginForm(AuthenticationForm):
	# email = EmailField(label=_("Email"), required=True,help_text=_("Required.")) #Email address is protected
	pass
	
	
	#although i write email field in models this field is compulsary for extra email authentication
	#if i want to add contact i can also add contact and other that should be in model
	
	#writing meta for this is optional
	
	# class Meta:
	#     model = User
	#     fields=('username','email','password')
		
   
	

class SignupForm(UserCreationForm):
	username=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Username",}))
	email=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Email",}))
	password1=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Enter Password",'type' : 'password'}))
	password2=forms.CharField(widget=forms.TextInput(attrs={"placeholder": " Confirm Password",'type' : 'password'}))
	

	
	class Meta:
		model = User
		

		fields = ('username','email','password1','password2',)#'__all__' also
	 
		#email fifeld is added later
		
		#help_text will remove the default text in signup page
		help_texts= {
			'username':None,
			# 'email':"Your email should contain @" if i add email and wants help_texts for that
		   #to remove help text of password and password2 go to UserCreationForm  and comment help_text in 
		}
