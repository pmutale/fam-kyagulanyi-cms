from settings.environ.base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = ['kirumba.herokuapp.com', ]

DATABASES = {'default': dj_database_url.config(default=os.environ.get('POSTGRES_URL'))}

STATIC_ROOT = os.path.join(BASE_DIR, "static/assets")
