#import django_heroku

from settings.environ.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ["kirumba.herokuapp.com", "3.8.232.46", "kirumba.org" ]

#if os.environ.get('AWS_ENV', None):
DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql_psycopg2',
            'NAME': 'mwebaza_enterprise',
            'USER': 'mwebaza',
            'PASSWORD': 'mwebaza',
            'HOST': 'localhost',
            'PORT': '5432',
        }
}   
#    DATABASES = {
#    	'default':
#	    read_pgpass(
#            	'mwebaza_enterprise',
#            	env='prd',
#            	host='localhost',
#            	engine='django.db.backends.postgresql_psycopg2')	
#    }
#else: 
 #   DATABASES = {
#         "default": dj_database_url.config(default=os.environ.get("POSTGRES_URL"), conn_max_age=600, ssl_require=True),
  #  }
   # DATABASES["default"]["ENGINE"] = "django.db.backends.postgresql_psycopg2"

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, "staticfiles")
# ]

APPEND_SLASH = False

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-prod.json"),
    }
}

#django_heroku.settings(locals())
