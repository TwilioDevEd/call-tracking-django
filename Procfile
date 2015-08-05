web: gunicorn sample_project.wsgi:application --log-file -
worker: celery -A sample_project.settings worker -l info
