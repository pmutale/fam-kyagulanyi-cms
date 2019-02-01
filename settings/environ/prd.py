import django_heroku

from settings.environ.base import *
import dj_database_url

DEBUG = True

ALLOWED_HOSTS = ['kirumba.herokuapp.com', '127.0.0.1' ]

DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('POSTGRES_URL'), conn_max_age=600, ssl_require=True),
}

DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'


STATIC_ROOT = os.path.join(BASE_DIR, "static")

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats-prd.json'),
    }
}
django_heroku.settings(locals())
