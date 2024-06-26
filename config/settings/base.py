"""
Django settings for TFRW project.

Generated by 'django-admin startproject' using Django 5.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os
import environ

from django.utils.translation import gettext_lazy as _

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent
APPS_DIR = BASE_DIR / "tfr"

env = environ.Env()
env.read_env(BASE_DIR / ".env")

# Default app name
APP_NAME = "TFR"

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

DEBUG = env.bool("DJANGO_DEBUG", False)

ADMINS = [("admin", "thaifilmreviewweb@gmail.com")]  # ERROR log receiver list

REST_FRAMEWORK = {
    "DEFAULT_PAGINATION_CLASS": "rest_framework.pagination.PageNumberPagination",
    "PAGE_SIZE": 10,
}


# Application definition

INSTALLED_APPS = [
    "daphne",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.humanize",
    "django_celery_beat",
    "django_filters",
    "rest_framework",
    "crispy_forms",
    "crispy_tailwind",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "django_htmx",
    "films.apps.FilmsConfig",
    "tfr.apps.TfrConfig",
    "reviews.apps.ReviewsConfig",
    "profiles.apps.ProfilesConfig",
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
    "allauth.account.middleware.AccountMiddleware",
    "django_htmx.middleware.HtmxMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
]

ROOT_URLCONF = "config.urls"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "unique-snowflake",
    }
}

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [APPS_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.request",
                "tfr.context_processors.settings",  # add SETTINGS object to context
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

AUTHENTICATION_BACKENDS = [
    # Needed to login by username in Django admin, regardless of `allauth`
    # "django.contrib.auth.backends.ModelBackend",
    "profiles.backends.CustomAuthenticationBackend",
    # `allauth` specific authentication methods, such as login by email
    # "allauth.account.auth_backends.AuthenticationBackend",
    "profiles.backends.CustomAllAuthAuthenticationBackend",
]

# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/
USE_I18N = True

LANGUAGE_CODE = "en"

LANGUAGES = [
    ("en", _("English")),
    ("th", _("Thai")),
]

LOCALE_PATHS = [BASE_DIR / "locale"]


TIME_ZONE = "Asia/Bangkok"

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATIC_URL = "static/"
MEDIA_URL = "media/"
MEDIA_ROOT = os.path.join(APPS_DIR, "media")

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

# ASGI
ASGI_APPLICATION = "config.asgi.application"
CHANNEL_LAYERS = {"default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}}

INTERNAL_IPS = [
    "127.0.0.1",
]

# EMAIL
# ------------------------------------------------------------------------------
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_TIMEOUT = 5

DEFAULT_FROM_EMAIL = "thaifilmreviewweb <noreply@thaifilmreviewweb.com>"
SERVER_EMAIL = DEFAULT_FROM_EMAIL
EMAIL_SUBJECT_PREFIX = "[thaifilmreviewweb] "
ACCOUNT_EMAIL_SUBJECT_PREFIX = "[thaifilmreviewweb] "  # from django-allauth

# AUTHENTICATION
# ------------------------------------------------------------------------------
LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/accounts/login/"

ACCOUNT_SIGNUP_REDIRECT_URL = "profiles:update"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"

ACCOUNT_CONFIRM_EMAIL_ON_GET = True
ACCOUNT_SESSION_REMEMBER = True

ACCOUNT_RATE_LIMITS = {}

ACCOUNT_AUTHENTICATION_METHOD = "email"
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_VERIFICATION = "optional"  # user can continue within the app but will receive an email to verify the email address
SOCIALACCOUNT_LOGIN_ON_GET = False

# CRISPY
# ------------------------------------------------------------------------------
CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
CRISPY_TEMPLATE_PACK = "tailwind"

# LOGGING
# ------------------------------------------------------------------------------
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "verbose": {
            "format": "{levelname} {asctime} {module} == {message}",
            "style": "{",
        },
    },
    "handlers": {
        "console": {
            "level": "INFO",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
        # "file_info": {
        #     "level": "INFO",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": "logs/tfr.info.log",
        #     "formatter": "verbose",
        #     "maxBytes": 1024**2,
        #     "backupCount": 2,
        # },
        # "file_error": {
        #     "level": "ERROR",
        #     "class": "logging.handlers.RotatingFileHandler",
        #     "filename": "logs/tfr.error.log",
        #     "formatter": "verbose",
        #     "maxBytes": 1024**2,
        #     "backupCount": 2,
        # },
        "mail_admins": {
            "level": "ERROR",
            "class": "django.utils.log.AdminEmailHandler",
            "include_html": False,
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            # "handlers": ["console", "file_info"],
        },
        "django.request": {
            "handlers": ["mail_admins"],
            # "handlers": ["mail_admins", "file_error"],
            "level": "ERROR",
            "propagate": False,
        },
    },
}

# CELERY
# -----------------------------------------------------
CELERY_TIMEZONE = TIME_ZONE
CELERY_BROKER_URL = env.str("CELERY_BROKER_URL", "redis://redis:6379")
CELERY_RESULT_BACKEND = CELERY_BROKER_URL
CELERY_RESULT_EXTENDED = True
CELERY_RESULT_BACKEND_ALWAYS_RETRY = True
CELERY_RESULT_BACKEND_MAX_RETRIES = 10
CELERY_ACCEPT_CONTENT = ["json"]
CELERY_TASK_SERIALIZER = "json"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_BEAT_SCHEDULER = "django_celery_beat.schedulers:DatabaseScheduler"

# LANGCHAIN
# -----------------------------------------------------
os.environ["OPENAI_API_KEY"] = env.str("OPENAI_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"] = "https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = env.str("LANGCHAIN_API_KEY")

# Custom Films app setting
# -----------------------------------------------------
NUM_REVIEWS_SUMMARY = 5
