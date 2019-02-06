import os

if os.environ.get('IS_HEROKU'): 
  from settings.environ.heroku import *
elif os.environ.get('AWS_ENV'):
  from settings.environ.aws import *
else:
  from settings.environ.dev import *
  
