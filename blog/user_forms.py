from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


# https://overiq.com/django-1-10/django-creating-users-using-usercreationform/
# Some reuse of code
class MyUserCreationForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150, label_suffix='')
	email = forms.EmailField(label='Enter email', label_suffix='')
	password1 = forms.CharField(label='Enter password', widget=forms.PasswordInput, label_suffix='')
	password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput, label_suffix='')

	def clean_username(self):
		username = self.cleaned_data['username'].lower()
		r = User.objects.filter(username=username)
		if r.count():
			raise ValidationError("Username already exists")
		return username

	def clean_email(self):
		email = self.cleaned_data['email'].lower()
		r = User.objects.filter(email=email)
		if r.count():
			raise ValidationError("Email already exists")
		return email

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		if password1 and password2 and password1 != password2:
			raise ValidationError("Password don't match")
		return password2

	def save(self, commit=True):
		user = User.objects.create_user(
			self.cleaned_data['username'],
			self.cleaned_data['email'],
			self.cleaned_data['password1']
		)
		return user


class BlogLoginForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
