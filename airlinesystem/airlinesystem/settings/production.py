from .base import *


ALLOWED_HOSTS = ["*"]
# CSRF_TRUSTED_ORIGINS = ["http://*.on-acorn.io", "https://*.on-acorn.io"]


# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.mysql",
#         "NAME": os.getenv("MARIADB_DATABASE"),
#         "USER": os.getenv("MARIADB_USER"),
#         "PASSWORD": os.getenv("MARIADB_ROOT_PASSWORD"),
#         "HOST": os.getenv("MARIADB_HOST"),
#         "PORT": os.getenv("MARIADB_PORT", 3306),
#     }
# }

DATABASES = {}
