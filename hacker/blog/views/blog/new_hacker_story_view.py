from django.shortcuts import render
from ...editor_forms import HackerStory


def new_story_view(request):
	if request.method == "POST":
		new_story_form = HackerStory(request.POST)
		if new_story_form.is_valid():
			story = new_story_form.save(commit=False)
			story.user_fk = request.user
			story.save()
			error = new_story_form.errors
		else:
			error = new_story_form.errors
	else:
		new_story_form = HackerStory()
		error = new_story_form.errors
	context = {'new_story_form': new_story_form, 'error': error}
	return render(request, 'blog/new_hacker_story.html', context=context)
