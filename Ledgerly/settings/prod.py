from .base import *

DEBUG =False
ALLOWED_HOSTS =[]


DATABASES = {
    "default": env.db("DATABASE_URL")  # required, no default
}


MAILERS = {
    'default': {
        'BACKEND': 'django.core.mail.backends.console.EmailBackend',
        "HOST": env("EMAIL_HOST"),
        "PORT": env.int("EMAIL_PORT", default=587),
        "USER": env("EMAIL_HOST_USER"),
        "PASSWORD": env("EMAIL_HOST_PASSWORD"),
        "USE_TLS": True,
    },
}

# Security hardening — the stuff `check --deploy` looks for
# Though I dont understand now
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")