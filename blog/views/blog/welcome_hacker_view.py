from django.shortcuts import render


def welcome_hacker_view(request):
	return render(request, 'blog/welcome_hacker_site.html', {'message': ''})
