web: newrelic-admin run-program gunicorn --pythonpath="$PWD/androidrest" wsgi:application
worker: python androidrest/manage.py rqworker default