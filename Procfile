release: python hacker/manage.py makemigrations
release: python hacker/manage.py migrate
web: gunicorn hacker/hacker.wsgi --log-file -