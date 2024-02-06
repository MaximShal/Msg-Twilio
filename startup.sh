#!/bin/bash

until netcat -z -v -w30 rabbitmq 5672; do
  echo "Waiting for RabbitMQ to come up..."
  sleep 5
done

echo "Starting migrations..."
python3 manage.py migrate
echo "Finished migrations"

echo "Collecting static files..."
python3 manage.py collectstatic --no-input

echo "Starting celery worker"
celery -A mt worker -l info &

echo "Starting celery beat"
celery -A mt beat -l INFO &

echo "Starting gunicorn"
python3 -m gunicorn mt.wsgi --bind 0.0.0.0:8000 --workers 2 --timeout 3600