from settings.environ.base import *

ALLOWED_HOSTS = ["mwebaza.localhost", "*"]

DEBUG = True

DATABASES = {
    'default':
        read_pgpass(
            'mwebaza_enterprise',
            env='dev',
            host='localhost',
            engine='django.db.backends.postgresql_psycopg2')
}

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

WEBPACK_LOADER = {
    'DEFAULT': {
        'BUNDLE_DIR_NAME': 'bundles/',
        'STATS_FILE': os.path.join(BASE_DIR, 'webpack-stats.json'),
    }
}
