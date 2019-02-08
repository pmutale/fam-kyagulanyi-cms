from settings.environ.base import *

DEBUG = False

ALLOWED_HOSTS = ["kirumba.herokuapp.com", "3.8.232.46", "kirumba.org"]

STATICFILES_DIRS = [os.path.join(BASE_DIR, "staticfiles")]

DATABASES = {}

APPEND_SLASH = False

STATIC_URL = "/static/"

STATIC_ROOT = os.path.join(BASE_DIR, "static/")

WEBPACK_LOADER = {
    "DEFAULT": {
        "BUNDLE_DIR_NAME": "bundles/",
        "STATS_FILE": os.path.join(BASE_DIR, "webpack-stats-prod.json"),
    }
}
