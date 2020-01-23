from django.contrib.auth import logout
from django.shortcuts import redirect


def user_logout_view(request):
	logout(request)
	return redirect('blog:welcome_hacker_view')
