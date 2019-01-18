from settings.environ.base import *

#ALLOWED_HOSTS = ['localhost:8000','127.0.0.1:8000', ]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

