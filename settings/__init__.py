import os

if os.environ.get("IS_HEROKU", None) or os.environ.get("AWS_ENV", None):
    from settings.environ.prd import *
else:
    from settings.environ.dev import *
