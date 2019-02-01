web: gunicorn familie.wsgi
release: python manage.py migrate
release: npm install && npm run build-production
