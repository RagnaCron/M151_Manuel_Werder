from django import forms


class BlogLoginForm(forms.Form):
	username = forms.CharField(label='Enter Username', min_length=4, max_length=150)
	password = forms.CharField(label='Enter Password', widget=forms.PasswordInput)
