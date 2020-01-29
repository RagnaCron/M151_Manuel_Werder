from django.shortcuts import render
from ...models import StoryModel


def show_hacker_stories_view(request):
	queryset = StoryModel.objects.all()
	context = {'stories': queryset}
	return render(request, 'blog/show_hacker_stories.html', context)


def show_story_view(request, story_id):
	story = StoryModel.objects.get(pk=story_id)
	return render(request, 'blog/show_hacker_story.html', context={'story': story})
