from django.shortcuts import render
from ...editor_forms import HackerStory
from ...models import StoryModel


def edit_my_hacker_story_view(request, my_story_id):
	model = StoryModel.objects.get(pk=my_story_id)
	if request.method == 'POST':
		edit_story_form = HackerStory(request.POST)
		if edit_story_form.is_valid():
			model.story_title = edit_story_form.clean_story_title()
			model.story_content = edit_story_form.clean_story_content()
			model.save()
			error = edit_story_form.errors
		else:
			error = edit_story_form.errors
	else:
		edit_story_form = HackerStory(instance=model)
		error = edit_story_form.errors
	context = {'edit_story_form': edit_story_form, 'error': error, 'my_story_id': my_story_id}
	return render(request, 'blog/edit_my_hacker_story.html', context=context)
