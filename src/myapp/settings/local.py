import os

from myapp.settings.base import *  # noqa

DEBUG = True
INSTALLED_APPS += ["django_extensions"]  # noqa
MIDDLEWARE += ["users.middleware.DevUserAutoLoginMiddleware"]  # noqa
DEV_USER_JWT = os.getenv("DJANGO_DEV_USER_JWT")
INTERNAL_IPS = ["127.0.0.1"]
