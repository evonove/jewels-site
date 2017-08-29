from .base import *


# security enforcement
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = env('DJANGO_SECURE_SSL_REDIRECT', True)
SESSION_COOKIE_SECURE = env('DJANGO_SESSION_COOKIE_SECURE', True)

# Using WhiteNoise storage backend which automatically takes care of gzipping
# static files, while creating unique names for each version so they can
# safely be cached forever
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

# emails
DEFAULT_EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', DEFAULT_EMAIL_BACKEND)
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_PORT = env('DJANGO_EMAIL_HOST_PORT')
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = env('DJANGO_EMAIL_USE_TLS', True)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

# logging
LOGGING['loggers'] = {
    'django': {
        'handlers': ['console', 'syslog'],
        'level': env('DJANGO_LOG_LEVEL', 'INFO'),
    },
    'jewels': {
        'handlers': ['logstash', 'syslog'],
        'level': env('JEWELS_LOG_LEVEL', 'INFO'),
    },
}

# Sentry
INSTALLED_APPS += (
    'raven.contrib.django.raven_compat',
)

RAVEN_CONFIG = {
    'dsn': env('SENTRY_DSN'),
}
