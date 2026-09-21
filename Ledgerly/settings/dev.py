from .base import *

DEBUG = True
ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]


# Database
# https://docs.djangoproject.com/en/6.1/ref/settings/#databases
DATABASES = {
    "default": env.db("DATABASE_URL")  # required, no default
}


MAILERS = {
    "default": {
        "BACKEND": "django.core.mail.backends.console.EmailBackend",
    }
}