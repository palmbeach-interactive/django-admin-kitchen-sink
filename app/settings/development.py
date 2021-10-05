from .base import *

INTERNAL_IPS = ("127.0.0.1",)

DEBUG = True

SITE_URL = "http://local.swissmusic.ch:3000"

##################################################################
# db
##################################################################
# chekck if runing in heroku environment
if 'DYNO' in os.environ:
    import dj_database_url
    db_from_env = dj_database_url.config(conn_max_age=500)
    DATABASES = {'default': {}}
    DATABASES['default'].update(db_from_env)

    ALLOWED_HOSTS = ['djaks.herokuapp.com',]


else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": "com_kitchensink_local",
            "USER": "",
            "HOST": "",
        }
    }


TEMPLATES[0]["OPTIONS"]["loaders"] = [
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
]

# DEFAULT_FILE_STORAGE = 'app.storage.MediaRootS3BotoStorage'
# AWS_S3_ENDPOINT_URL='https://ams3.digitaloceanspaces.com'
# AWS_ACCESS_KEY_ID = 'DWCSM6XYKXUUUTU2S35A'
# AWS_SECRET_ACCESS_KEY = '***'
# AWS_STORAGE_BUCKET_NAME = 'ch-swissmusic'

DEFAULT_FILE_STORAGE = "django.core.files.storage.FileSystemStorage"


##################################################################
# cache
##################################################################
CACHES = {
    "default": {"BACKEND": "django.core.cache.backends.dummy.DummyCache"},
    # 'default': {
    #     'BACKEND': 'django_redis.cache.RedisCache',
    #     'LOCATION': 'redis://127.0.0.1:6379/7',
    #     'OPTIONS': {
    #         'CLIENT_CLASS': 'django_redis.client.DefaultClient',
    #     },
    # },
}
#
# SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
# SESSION_CACHE_ALIAS = 'default'


##################################################################
# queues
##################################################################
CELERY_BROKER_URL = "redis://localhost:6379/6"
CELERY_RESULT_BACKEND = "redis://localhost:6379/6"
CELERY_TASK_SERIALIZER = "json"
CELERY_ACCEPT_CONTENT = ["json"]

##################################################################
# email
##################################################################
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = 'smtp.sendgrid.net'
# EMAIL_HOST_USER = ''
# EMAIL_HOST_PASSWORD = ''
# EMAIL_PORT = 587
# EMAIL_USE_TLS = True

INSTALLED_APPS += [
    # "dev",
    # 'debug_toolbar',
    "django_extensions",
]

MIDDLEWARE += [
    #'debug_toolbar.middleware.DebugToolbarMiddleware',
]

# DEBUG_TOOLBAR_PANELS = [
#     #'cachalot.panels.CachalotPanel',
# ]

# this fixes strange behaviour when running app through gunicorn
DEBUG_TOOLBAR_PATCH_SETTINGS = False


WERKZEUG_DEBUG_PIN = "off"

DEVSERVER_MODULES = []

NOTEBOOK_ARGUMENTS = ["--notebook-dir", "notebooks"]

IPYTHON_ARGUMENTS = ["--debug"]

LOGGING_ = {
    "version": 1,
    "disable_existing_loggers": False,
    "root": {"level": "WARNING", "handlers": LOGGING_ROOT_HALNDLERS},
    "formatters": {
        "default": {"format": "%(levelname)s %(module)s %(message)s"},
        "verbose": {
            # "format": "%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s",
            "format": "%(asctime)s %(levelname)s\t%(name)s\t%(funcName)s:%(lineno)s - %(message)s",
        },
    },
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
            "formatter": "verbose",
        },
    },
    "loggers": {
        "django.db.backends": {
            "level": "WARNING",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.request": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
        "django.template": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "sentry.errors": {
            "level": "INFO",
            "handlers": ["console"],
            "propagate": False,
        },
        "webpack": {
            "level": "DEBUG",
            "handlers": ["console"],
            "propagate": False,
        },
    },
}

QUERYCOUNT = {
    "THRESHOLDS": {
        "MEDIUM": 20,
        "HIGH": 50,
        "MIN_TIME_TO_LOG": 0,
        "MIN_QUERY_COUNT_TO_LOG": 0,
    },
    "IGNORE_REQUEST_PATTERNS": [
        r"^/admin/",
        r"^/static/",
    ],
    "IGNORE_SQL_PATTERNS": [
        r"django_",
        r"cms_",
        r"menus_",
        r"account_",
    ],
    "DISPLAY_DUPLICATES": 3,
}
