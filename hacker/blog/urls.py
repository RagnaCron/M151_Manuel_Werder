from django.urls import path
from .views.blog import welcome_hacker_view, user_login_view, user_sign_in_view, user_logout_view, new_hacker_story_view

app_name = 'blog'
urlpatterns = [
	path('', welcome_hacker_view.welcome_hacker_view, name='welcome_hacker_view'),
	path('login/', user_login_view.user_login_view, name='user_login_view'),
	path('register/', user_sign_in_view.user_sign_up_view, name='user_sign_up_view'),
	path('logout', user_logout_view.user_logout_view, name='user_logout_view'),
	path('story/new/', new_hacker_story_view.new_story_view, name='new_story_view'),
]
