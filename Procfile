web: sh -c "python manage.py migrate --noinput && python manage.py collectstatic --noinput && gunicorn catalogo_web.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120"
