from django.contrib import auth
from django.contrib.auth.models import User
from django.shortcuts import render


def user_sign_in(request):
	return render(request, 'blog/user_sign_in.html', {'message': ''})
