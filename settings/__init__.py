import os
if not os.environ.get('IS_HEROKU', None):
    from settings.environ.prd import *
else:
    from settings.environ.dev import *
