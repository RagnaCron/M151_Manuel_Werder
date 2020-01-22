from django.contrib.auth.models import User
from django.db import models
from froala_editor.fields import FroalaField


# Create your models here.
class StoryModel(models.Model):
	user_fk = models.ForeignKey(User, on_delete=models.CASCADE)
	story_title = models.CharField(unique=True, max_length=50)
	story_content = FroalaField()
# 	ToDo: Creation DATE
