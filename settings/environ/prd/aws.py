from settings.environ.prd.prd import *


DATABASES["default"] = read_pgpass(
    "mwebaza_enterprise",
    env="dev",
    host="localhost",
    engine="django.db.backends.postgresql_psycopg2",
)
