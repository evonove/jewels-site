from .base import *


# removing security enforcement in development mode
DEBUG = True
SECRET_KEY = env('DJANGO_SECRET_KEY', '1234567890')

INTERNAL_IPS = ['127.0.0.1']
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# enabling console loggers
LOGGING['loggers'] = {
    'django': {
        'handlers': ['console'],
        'level': env('DJANGO_LOG_LEVEL', 'INFO'),
    },
    'jewels': {
        'handlers': ['console'],
        'level': env('JEWELS_LOG_LEVEL', 'DEBUG'),
    },
}
