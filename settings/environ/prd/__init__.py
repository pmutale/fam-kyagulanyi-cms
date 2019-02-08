import os

if os.environ.get("IS_HEROKU", None):
    from settings.environ.prd.heroku import *
elif os.environ.get("AWS_ENV", None):
    from settings.environ.prd.aws import *
