release: python app/manage.py migrate
web: gunicorn --pythonpath app project.wsgi --log-file -
