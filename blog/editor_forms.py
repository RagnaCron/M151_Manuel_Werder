from django import forms
from froala_editor.widgets import FroalaEditor
from .models import StoryModel


class HackerStory(forms.ModelForm):
	class Meta:
		model = StoryModel
		fields = ('story_title', 'story_content')

	story_title = forms.CharField(min_length=4, max_length=50)
	story_content = forms.CharField(widget=FroalaEditor)

	def clean_story_title(self):
		return self.cleaned_data.get('story_title')

	def clean_story_content(self):
		return self.cleaned_data.get('story_content')

	# def __init__(self, story_title=None, story_content=None):
	# 	super().__init__()
	# 	story_title = forms.CharField(min_length=4, max_length=50, initial=story_title)
	# 	story_content = forms.CharField(widget=FroalaEditor, initial=story_content)

	# def set_initial(self, title, content):
	# 	story_title.initial = title
	# 	story_content.initial = content

# story_content = forms.CharField(widget=FroalaEditor(options={
# 	'toolbarInline': True,
# }))
