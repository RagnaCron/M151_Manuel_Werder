from django import forms
from froala_editor.widgets import FroalaEditor
from .models import StoryModel


class HackerStory(forms.ModelForm):
	class Meta:
		model = StoryModel
		fields = ('story_title', 'story_content')

	story_title = forms.CharField(min_length=4, max_length=50)
	story_content = forms.CharField(widget=FroalaEditor)
	# story_content = forms.CharField(widget=FroalaEditor(options={
	# 	'toolbarInline': True,
	# }))
