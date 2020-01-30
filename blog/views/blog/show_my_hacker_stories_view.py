from django.shortcuts import render
from ...models import StoryModel


def show_my_hacker_stories_view(request):
	queryset = StoryModel.objects.filter(user_fk=request.user.pk)
	context = {'my_stories': queryset}
	return render(request, 'blog/show_my_hacker_stories.html', context)
