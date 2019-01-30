import os
if os.environ['IS_HEROKU']:
    from settings.environ.prd import *
else:
    from settings.environ.dev import *
