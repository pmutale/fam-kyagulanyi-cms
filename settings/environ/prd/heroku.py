import dj_database_url
import django_heroku

from settings.environ.prd.prd import *

DATABASES = {
    "default": dj_database_url.config(
        default=os.environ.get("POSTGRES_URL"), conn_max_age=600, ssl_require=True
    )
}

DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"

django_heroku.settings(locals())
