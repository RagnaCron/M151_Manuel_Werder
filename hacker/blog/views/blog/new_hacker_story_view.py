from django.shortcuts import render


def new_story_view(request):
	return render(request, 'blog/new_hacker_story.html', {'message': ''})
