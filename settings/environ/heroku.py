from settings.environ.prd import *
import django_heroku

django_heroku.settings(local())
