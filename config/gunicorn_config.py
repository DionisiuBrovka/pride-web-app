command = 'home/www/project-pride/proj-env/bin/gunicorn'
pythonpath = 'home/www/project-pride/pride-web-app/webapp'
bind = '127.0.0.1:8765'
workers = 3
user = 'www'
raw_env = 'DJANGO_SETTINGS_MODULE=webapp.settings'