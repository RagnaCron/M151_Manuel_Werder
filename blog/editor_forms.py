from django import forms
from froala_editor.widgets import FroalaEditor
from .models import StoryModel


class HackerStory(forms.ModelForm):
	class Meta:
		model = StoryModel
		fields = ('story_title', 'story_content')

	story_title = forms.CharField(min_length=4, max_length=50)
	story_content = forms.CharField(widget=FroalaEditor, min_length=1)

	def clean_story_title(self):
		return self.cleaned_data.get('story_title')

	def clean_story_content(self):
		return self.cleaned_data.get('story_content')

# story_content = forms.CharField(widget=FroalaEditor(options={
# 	'toolbarInline': True,
# }))
