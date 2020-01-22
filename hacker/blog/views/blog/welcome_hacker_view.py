from django.shortcuts import render

# Create your views here.


def welcome_hacker_view(request):
	return render(request, 'blog/welcome_hacker_site.html', {'message': ''})
