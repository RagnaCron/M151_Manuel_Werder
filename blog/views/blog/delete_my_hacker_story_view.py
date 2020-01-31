from django.shortcuts import render, redirect
from ...editor_forms import HackerStory
from ...models import StoryModel


def delete_my_hacker_story_view(request, delete_id):
	model = StoryModel.objects.get(pk=delete_id)
	context = {'story': model, 'delete_id': delete_id}
	if request.method == 'POST':
		model.delete()
		return redirect('blog:show_my_hacker_stories_view')
	return render(request, 'blog/delete_my_hacker_story.html', context=context)
