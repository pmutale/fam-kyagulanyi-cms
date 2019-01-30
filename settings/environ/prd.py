from settings.environ.base import *
import dj_database_url

DEBUG = False

DATABASES = {'default': dj_database_url.config(default=os.environ['POSTGRES_URL'])}

STATIC_ROOT = os.path.join(BASE_DIR, "static/assets")
