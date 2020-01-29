from django.shortcuts import render
from django.views.generic.list import ListView
from ...editor_forms import HackerStory
from ...models import StoryModel


class HackerStoriesListView(ListView):
	template_name = 'blog/show_hacker_stories.html'
	model = StoryModel
	context_object_name = 'stories'
	paginate_by = 10


def show_hacker_stories_view(request):

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
	return render(request, 'blog/show_hacker_stories.html')
