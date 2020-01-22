from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render

from blog.forms.blog.user_sign_up_form import MyUserCreationForm


def user_sign_up_view(request):
	if request.method == 'POST':
		user_sign_up_form = MyUserCreationForm(request.POST)
		if user_sign_up_form.is_valid():
			user_sign_up_form.save()
			auth.login(request, user=User.objects.get(username=user_sign_up_form.cleaned_data['username']))
			return render(request, 'blog/welcome_hacker_site.html', {'message': 'Successful User Signup.'})
	else:
		user_sign_up_form = MyUserCreationForm()
	context = {'user_sign_up_form': user_sign_up_form, 'errors': user_sign_up_form.errors}
	return render(request, 'blog/user_sign_up.html', context=context)
