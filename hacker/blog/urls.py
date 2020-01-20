from django.urls import path
from .views.blog import welcome_hacker_view

app_name = 'blog'
urlpatterns = [
	path('', welcome_hacker_view.welcome_hacker, name='welcome_hacker'),
]
