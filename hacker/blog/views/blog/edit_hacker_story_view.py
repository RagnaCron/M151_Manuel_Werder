from django.shortcuts import render
from ...editor_forms import HackerStory


def edit_story_view(request):
	# if request.method == "POST":
	# 	story_form = HackerStory(request.POST)
	# 	if story_form.is_valid():
	# 		story = story_form.save(commit=False)
	# 		story.user_fk = request.user
	# 		story.save()
	# 		error = story_form.errors
	# 	else:
	# 		error = story_form.errors
	# else:
	# 	story_form = HackerStory()
	# 	error = story_form.errors
	# context = {'new_story_form': story_form, 'error': error}
	# return render(request, 'blog/new_hacker_story.html', context=context)
	return render(request, 'blog/edit_hacker_story.html')
