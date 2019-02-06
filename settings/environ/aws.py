from settings.environ.prd import *

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
