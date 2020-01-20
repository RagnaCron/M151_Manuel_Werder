from django.urls import path
from .views.blog import welcome_hacker_view, user_login_view, user_sign_in_view, user_logout_view

app_name = 'blog'
urlpatterns = [
	path('', welcome_hacker_view.welcome_hacker, name='welcome_hacker'),
	path('login/', user_login_view.user_login, name='user_login'),
	path('register/', user_sign_in_view.user_sign_up, name='user_sign_up'),
	path('logout', user_logout_view.user_logout, name='user_logout'),
]
