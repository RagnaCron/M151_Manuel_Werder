from django.contrib.auth import authenticate, login
from django.shortcuts import render
from blog.forms.blog.blog_login_form import BlogLoginForm


def user_login_view(request):
	if request.method == 'POST':
		user_login_form = BlogLoginForm(request.POST)
		if user_login_form.is_valid():
			username = user_login_form.cleaned_data.get('username')
			password = user_login_form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				return render(request, 'blog/welcome_hacker_site.html', {'message': 'Your login was successful.'})
			error = 'Username or Password is wrong.'
		else:
			error = user_login_form.errors
	else:
		user_login_form = BlogLoginForm()
		error = user_login_form.errors
	context = {'user_login_form': user_login_form, 'error': error}
	return render(request, 'blog/user_login.html', context=context)
