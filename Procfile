release: python -m pip freeze && python src/manage.py migrate
web: gunicorn config.wsgi --chdir src --log-file -
