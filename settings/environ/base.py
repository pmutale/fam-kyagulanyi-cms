from settings.core import *

INSTALLED_APPS = [

    "djangocms_admin_style",
    "django.contrib.admin",
    "django.contrib.sites",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",

    # Django CMS
    "cms",
    "menus",
    "treebeard",
    "sekizai",
    "filer",
    "easy_thumbnails",
    "mptt",
    "djangocms_text_ckeditor",
    "djangocms_link",
    "djangocms_file",
    "djangocms_picture",
    "djangocms_video",
    "djangocms_googlemap",
    "djangocms_snippet",
    "djangocms_style",
    "djangocms_column",

    # Django Rest Framework
    "rest_framework",
    "rest_framework_swagger",
    "webpack_loader",

    # My Apps


]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.locale.LocaleMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "cms.middleware.user.CurrentUserMiddleware",
    "cms.middleware.page.CurrentPageMiddleware",
    "cms.middleware.toolbar.ToolbarMiddleware",
    "cms.middleware.language.LanguageCookieMiddleware",
]

ROOT_URLCONF = "familie.urls"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["familie/templates",
                 os.path.join(BASE_DIR, 'templates')],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "sekizai.context_processors.sekizai",
                # "cms.middleware.utils.ApphookReloadMiddleware",
                # "cms.context_processors.cms_settings ",
            ]
        },
    }
]
# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = "en"

TIME_ZONE = "UTC"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = "/static/"

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)

MEDIA_URL = "/media/"

MEDIA_ROOT = os.path.join(BASE_DIR, "media")

LANGUAGES = [
    ("en", "English"),
    ("sw", "Swahili"),
    ("nl", "Nederlands"),

]

CMS_TEMPLATES = [
    ("familie/homepage.html", "Home Page"),
    ("familie/contentpage.html", "Content Page"),
]

THUMBNAIL_HIGH_RESOLUTION = True

THUMBNAIL_PROCESSORS = (
    "easy_thumbnails.processors.colorspace",
    "easy_thumbnails.processors.autocrop",
    "filer.thumbnail_processors.scale_and_crop_with_subject_location",
    "easy_thumbnails.processors.filters"
)


def read_pgpass(dbname, host=None, port=None, engine=None, env=None):
    """
    Intends to read the .pgpass file stored on the local environment. Its the intentions
    that everyone make that file on their dev environment
    ==> http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    :param engine:
    :param port:
    :param host:
    :param dbname: Database name
    :return:
    """
    import sys
    from pathlib import Path

    home_path = str(Path.home())

    no_database_found = ("""
        Your {path}/.pgpass file doesn"t have database "{dbname}" for host "{host}:{port}".

        To switch to a PostgreSQL database, add a line to the ~/.pgpass file
        containing it"s credentials.
        See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
        """.format(dbname=dbname, path=home_path, host=host or "*", port=port or "*"))
    no_pgpass_notification = ("""
    You don"t have a {0}/.pgpass file so. Please create one!

    To switch to a PostgreSQL database, create a ~/.pgpass file
    containing it"s credentials.
    See http://www.postgresql.org/docs/9.3/static/libpq-pgpass.html
    """.format(home_path))

    try:
        pgpass = os.path.join(home_path, ".pgpass") if not 'dev' in env else os.path.join(BASE_DIR, '.secrets/.pgpass')
        pgpass_lines = open(pgpass).read().split()
    except IOError:
        # Print instructions
        print(no_pgpass_notification)
    else:
        for match in (dbname, "*"):
            for line in pgpass_lines:
                words = line.strip().split(":")
                if words[2] == match and words[0] == (host or words[0]) and words[1] == (port or words[1]):
                    return dict(ENGINE=engine,
                                NAME=dbname,
                                USER=words[3],
                                PASSWORD=words[4],
                                HOST=words[0],
                                PORT=words[1],
                                )
        print(no_database_found)
    return sys.exit("Error: You don't have a database setup, Please create a ~/.pgpass file ")
