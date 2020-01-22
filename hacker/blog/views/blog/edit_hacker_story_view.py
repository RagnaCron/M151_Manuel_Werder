from django.shortcuts import render
from ...editor_forms import HackerStory


def edit_story_view(request):
	# if request.method == "POST":
	# 	edit_story_form = HackerStory(request.POST)
	# 	if edit_story_form.is_valid():
	# 		story = edit_story_form.save(commit=False)
	# 		story.user_fk = request.user
	# 		story.save()
	# 		error = edit_story_form.errors
	# 	else:
	# 		error = edit_story_form.errors
	# else:
	# 	edit_story_form = HackerStory()
	# 	error = edit_story_form.errors
	# context = {'new_story_form': edit_story_form, 'error': error}
	# return render(request, 'blog/new_hacker_story.html', context=context)
	return render(request, 'blog/edit_hacker_story.html')
