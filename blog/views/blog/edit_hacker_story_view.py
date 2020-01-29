from django.shortcuts import render
from ...editor_forms import HackerStory
from ...models import StoryModel


def show_my_hacker_stories_view(request):
	queryset = StoryModel.objects.filter(user_fk=request.user.pk)
	print(queryset)
	context = {'my_stories': queryset}
	return render(request, 'blog/show_my_hacker_stories.html', context)


def edit_my_hacker_story_view(request):
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
