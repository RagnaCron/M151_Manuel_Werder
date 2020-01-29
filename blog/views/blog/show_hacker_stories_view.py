from django.shortcuts import render
from ...models import StoryModel


def show_hacker_stories_view(request):
	queryset = StoryModel.objects.all()
	context = {'stories': queryset}
	return render(request, 'blog/show_hacker_stories.html', context)


def show_story_view(request, story_title):
	story = StoryModel.objects.get(story_title=story_title)
	return render(request, 'blog/show_hacker_story.html', context={'story': story})
